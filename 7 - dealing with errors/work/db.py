import sqlite3
from types import SimpleNamespace

import logging

logger = logging.getLogger(__name__)

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
    logger.info('opening db')
    con = sqlite3.connect('7 - dealing with errors/work/application.db')
    cur = con.cursor()
    logger.info(f'{con=}')
    logger.info(f'{cur=}')

    cur.execute('SELECT * FROM blogs where public=1')

    records = cur.fetchall()
    logger.info(f'{records=}')
    result = list(map(blog_lst_to_json, records))
    logger.info(f'{result=}')

    con.close()
    return result


def fetch_blog(id: str) -> dict:
    """
    returns a single recordset
    """
    try:
        con = sqlite3.connect('application.db')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM blogs where id='{id}'")
        result = cur.fetchone()

        if result is None:
            raise NotFoundError(f'Unable to find blog with id {id}')

        data = blog_lst_to_json(result)
        if not SimpleNamespace(**data).public:
            raise NotAuthorizedError(f'You are not allowed to access blog with id {id}')                    
        return data
    
    except sqlite3.OperationalError as oe:
        print(oe)
        raise NotFoundError(f'Unable to find blog with id {id}')
    finally:
        con.close()
