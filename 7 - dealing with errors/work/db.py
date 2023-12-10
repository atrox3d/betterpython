import sqlite3
from types import SimpleNamespace

import logging

logger = logging.getLogger(__name__)

class SQLite:
    
    def __init__(self, file) -> None:
        logger.info(f'initializing context manager: {file=}')
        self.file = file
    
    def __enter__(self):
        logger.info('opening connection')
        self.conn = sqlite3.connect(self.file)
        logger.info('returning cursor')
        return self.conn.cursor()
    
    def __exit__(self, type, value, traceback):
        logger.info('closing connection')
        logger.info(f'{type=}')
        logger.info(f'{value=}')
        logger.info(f'{traceback=}')
        self.conn.close()


class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def blog_lst_to_json(item: list) -> dict:
    """
    returns a dict from a single recordset
    """
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

def fetch_blogs() -> list[dict]:
    """
    return a list of recordsets matching the query
    """
    try:
        with SQLite('7 - dealing with errors/work/application.db') as cur:
            logger.info(f'{cur=}')

            cur.execute('SELECT * FROM blogs where public=1')

            records = cur.fetchall()
            logger.info(f'{records=}')
            result = list(map(blog_lst_to_json, records))
            logger.info(f'{result=}')

            return result
    except Exception as e:
        logger.exception()
        return []

def fetch_blog(id: str) -> dict:
    """
    returns a single recordset
    """
    try:
        with SQLite('7 - dealing with errors/work/application.db') as cur:

            query=(f"SELECT * FROM blogs where id='{id}'")
            logger.info(query)
            cur.execute(query)

            result = cur.fetchone()
            logger.info(f'{result=}')

            if result is None:
                message = f'Unable to find blog with id {id}'
                logger.exception(message)
                raise NotFoundError(message)
            data = blog_lst_to_json(result)
            if not SimpleNamespace(**data).public:
                message = f'You are not allowed to access blog with id {id}'
                logger.exception(message)
                raise NotAuthorizedError(message)                    
            return data
        
    except sqlite3.OperationalError as oe:
        message = f'Unable to find blog with id {id}'
        logger.exception(message)
        raise NotFoundError(message)
