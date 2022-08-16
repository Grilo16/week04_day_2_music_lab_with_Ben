from db.run_sql import run_sql
from models.album_class import Album



def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(**row)
        albums.append(album)
    return albums

def add_to_db(object):
    sql = "INSERT INTO albums (title, artist) VALUES (%s, %s) RETURNING id"
    
    values = [object.title, object.artist]
    object.id = run_sql(sql, values)[0][0]
    return object


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
    
def select_by_id(id):
    sql = "SELECT * FROM albums WHERE id=%s"
    values = [id]
    try:
        row_result = run_sql(sql, values)[0]
    except IndexError:
        row_result = None
        print("not enough items in list")
    if row_result != None:
        album = Album(**row_result)
        return album
    return print("album not found")

def update(album):
    sql = "UPDATE albums SET (title, artist) = (%s, %s) WHERE ID = %s"
    values = [album.title,album.artist,album.id]
    run_sql(sql, values)
    
def delete_one(album):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [album.id]
    run_sql(sql, values)