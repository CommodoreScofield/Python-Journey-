class Movie:
    def __init__(self, title, genre, actor, year):
        self.title = title
        self.genre = genre
        self.actor = actor
        self.year = year

    def get_movie(self):
        print(f"{self.title} {self.genre} {self.actor} {self.year}")

movie_uno = Movie("Dhurander: The Revenge ", "Adventure"," Ranveer Singh ", 2026 )
movie_dos = Movie("Coolie", "Action", "Ranji", 2025 )
movie_tres = Movie("Widows Bay","Horror","Dont Know",2026)
movie_uno.get_movie()
movie_dos.get_movie()
movie_tres.get_movie()
                                                                                                                                                                                                                        