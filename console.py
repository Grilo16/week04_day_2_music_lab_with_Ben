from models.album_class import Album
import repositories.album_repository as album_repo


album = Album("Rick Astley", "Whenever you need somebody")
album.title = "Oh yeah,  Blaaaaze"
album_repo.update(album)

album_repo.add_to_db(album)
print()
album_repo.select_by_id(420)
album3 = album_repo.select_by_id(3)
album_repo.delete_one(album3)
# album_repo.delete_all()



# print(album_repo.select_all())
