import sqlite3

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
    con = sqlite3.connect('application.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM blogs where public=1')

    result = list(map(blog_lst_to_json, cur.fetchall()))

    con.close()
    return result


def fetch_blog(id: str) -> dict:
    """
    returns a single recordset
    """
    con = sqlite3.connect('application.db')
    cur = con.cursor()

    cur.execute(f"SELECT * FROM blogs where id='{id}'")
    result = cur.fetchone()
    data = blog_lst_to_json(result)

    con.close()
    return data

