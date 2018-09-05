from .models import Gist


def search_gists(db_connection, **kwargs):
    SQL_QUERY = 'SELECT * from gists'
    git_id = False
    create = False
    if 'errormessage' in kwargs:
        pass
    
    if 'github_id' in kwargs:
        SQL_QUERY += ' WHERE github_id = ?'
        git_id = True
    
    if 'created_at' in kwargs:
        if git_id:
            SQL_QUERY += ' AND WHERE created_at = ?'
        else:
            SQL_QUERY += ' WHERE created_at = ?' 
        
        create = True
    
        
    params = [vals for vals in kwargs.values()]
    
    if len(params) < 1:
        cursor = db_connection.execute(SQL_QUERY)

    else:
        cursor = db_connection.execute(SQL_QUERY, params)
        
    return cursor.fetchall()
        
