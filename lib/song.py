class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    
    
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
        
    # solved using class methods and instance methods for the following:
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
      
    
    @classmethod
    def add_song_to_count(cls):
        cls.count +=1
        
    # @classmethod
    # def add_to_genres(cls, genre):
    #     if genre not in cls.genres:
    #         cls.genres.append(genre)
            
    # @classmethod
    # def add_to_artists(cls, artist):
    #     if artist not in cls.artists:
    #         cls.artists.append(artist)

    # @classmethod
    # def add_to_genre_count(cls,genre):
    #     cls.genre_count[genre] = cls.genre_count.get(genre,0)+1
        
    # @classmethod
    # def add_to_artist_count(cls,artist):
    #     cls.artist_count[artist] = cls.artist_count.get(artist,0)+1
    
    def add_to_genres(self):
        if self.genre not in self.genres:
            self.genres.append(self.genre)
            
    def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    def add_to_genre_count(self):
        self.genre_count[self.genre] = self.genre_count.get(self.genre,0)+1
        
    def add_to_artist_count(self):
        self.artist_count[self.artist] = self.artist_count.get(self.artist,0)+1
       



