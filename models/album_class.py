class Album():
    def __init__(self, artist, title, id = None):
        self.artist = artist
        self.title = title
        self.id = id
        
    def __str__(self):
        return f"{self.artist} made {self.title} the id is {self.id}"        
