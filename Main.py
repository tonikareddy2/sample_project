import pyodbc
from Entity.movie import Movie
from DAO.movie_service import MovieService

server_name = "DESKTOP-P8QAI2N\SQLEXPRESS"
database_name = "HexawareMovieDB"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
# print(conn_str)1
conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()
# cursor.execute("SELECT 1")
# print("Database connection is successful")


# class MovieServices:

#     def read_movies(self):
#         cursor.execute("SELECT * FROM Movies")
#         movies = cursor.fetchall()
#         for movie in movies:
#             print(movie)

#         # getting 1 row at a time
#         for row in cursor:
#             print(row)

#     def create_movie(self, n, y, d):
#         cursor.execute(
#             "INSERT INTO Movies (Title, Year, DirectorId) VALUES(?,?,?)",
#             (n, y, d),
#         )
#         conn.commit()  # permanently inserts the value
#         print("Movie inserted successfully.")

#     def delete_movie(self, id):
#         cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (id,))
#         conn.commit()
#         print("Movie deleted successfully.")

#     def update_movie(self, title, year, director_id, movie_id):
#         cursor.execute(
#             """
#         Update Movies
#         Set Title = ?, Year = ?, DirectorId = ?
#         where MovieId = ?
#         """,
#             (title, year, director_id, movie_id),
#         )
#         conn.commit()


# def Movie_Management():
#     Movie_service = MovieServices()
#     while True:
#         print("1. Create a movie")
#         print("2. Delete a movie")
#         print("3. Read movies")
#         print("4. Update Movie")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter the movie name: ")
#             year = int(input("Enter the year: "))
#             director_id = int(input("Enter the director ID: "))
#             Movie_service.create_movie(name, year, director_id)
#         elif choice == "2":
#             Movie_service.read_movies()
#             MovieId = int(input("Enter the MovieId: "))
#             Movie_service.delete_movie(MovieId)
#         elif choice == "3":
#             Movie_service.read_movies()
#         elif choice == "4":
#             Movie_service.read_movies()
#             movie_id = int(input("Please enter movie's id: "))
#             title = input("Please enter movie title: ")
#             year = int(input("Please enter movie year: "))
#             director_id = int(input("Please enter movie director's id: "))
#             Movie_service.update_movie(title, year, director_id, movie_id)
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")


# Service - Function that talk to DB | Layer that interacts with DB


# Encapsulation
# class MovieService:
#     def read_movies(self):
#         cursor.execute("Select * from Movies")
#         # movies = cursor.fetchall() # Get all data
#         # for movie in movies:
#         #     print(movie)

#         # Get data one row at a time
#         for row in cursor:
#             print(row)

#     # Task 1
#     # Get the data from the user
#     # Clue: Use arguments
#     def create_movie(self, movie):
#         cursor.execute(
#             "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
#             (movie.title, movie.year, movie.director_id),
#         )
#         conn.commit()  # Permanent storing | If no commit then no data

#     def update_movie(self, movie, movie_id):
#         cursor.execute(
#             """
#             Update Movies
#             Set Title = ?, Year = ?, DirectorId = ?
#             where MovieId = ?
#             """,
#             (movie.title, movie.year, movie.director_id, movie_id),
#         )
#         conn.commit()  # Permanent storing | If no commit then no data

#     # Task 2
#     # Delete a movie from the db by getting the id from user
#     def delete_movie(self, movie_id):
#         cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
#         conn.commit()


class DirectorService:
    pass


class ActorService:
    pass


# Entity / Model
# Encapsulation - Movie data
# class Movie:
#     def __init__(self, title, year, director_id):
#         self.title = title
#         self.year = year
#         self.director_id = director_id


class Director:
    pass


class Actor:
    pass


# Main menu
# 1. Movie Management
# 2. Director Management
# 3. Actor Management
# 4. Exit


# Task 3
# Movie Management Menu
# 1. Add a Movie
# 2. View All Movies
# 3. Update a Movie  (Task 4)
# 4. Delete a Movie
# 5. Back

# C - Create
# R - Read
# U - Update
# D - Delete


def movie_menu():
    movie_service = MovieService(conn)

    while True:
        print(
            """      
        1. Add a Movie
        2. View all Movies
        3. Update a Movie  
        4. Delete a Movie
        5. Back to main menu
                """
        )
        choice = int(input("Please choose from above options: "))

        if choice == 1:
            title = input("Please enter movie title: ")
            year = int(input("Please enter movie year: "))
            director_id = int(input("Please enter movie director's id: "))
            new_movie = Movie(title, year, director_id)
            movie_service.create_movie(new_movie)
        elif choice == 2:
            movie_service.read_movies()
        if choice == 3:
            movie_id = int(input("Please enter movie's id: "))
            title = input("Please enter movie title: ")
            year = int(input("Please enter movie year: "))
            director_id = int(input("Please enter movie director's id: "))
            updated_movie = Movie(title, year, director_id)
            movie_service.update_movie(updated_movie, movie_id)
        elif choice == 4:
            movie_id = int(input("Please tell a movie id to delete: "))
            movie_service.delete_movie(movie_id)
        elif choice == 5:
            break


def director_menu():
    pass


def actor_menu():
    pass


# Task 5 - Keep it in loop
if __name__ == "__main__":
    print("Welcome to the movies app")

    while True:
        print(
            """      
            1. Movie Management
            2. Director Management
            3. Actor Management
            4. Exit
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            movie_menu()
        elif choice == 2:
            director_menu()
        elif choice == 3:
            actor_menu()
        elif choice == 4:
            break

    # Clean up code
    # cursor.close()
    conn.close()
