import pyodbc

server_name = "DESKTOP-P8QAI2N\SQLEXPRESS"
database_name = "HexawareMovieDB"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
# print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT 1")
print("Database connection is successful")


def read_movies():
    cursor.execute("SELECT * FROM Movies")
    # movies = cursor.fetchall()
    # for movie in movies:
    #     print(movie)

    # getting 1 row at a time
    for row in cursor:
        print(row)


def create_movie(n, y, d):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES(?,?,?)",
        (n, y, d),
    )
    conn.commit()  # permanently inserts the value
    print("Movie inserted successfully.")


def delete_movie(id):
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (id,))
    conn.commit()
    print("Movie deleted successfully.")


def update_movie(title, year, director_id, movie_id):
    cursor.execute(
        """
        Update Movies
        Set Title = ?, Year = ?, DirectorId = ?
        where MovieId = ?
        """,
        (title, year, director_id, movie_id),
    )
    conn.commit()


if __name__ == "__main__":
    while True:
        print("1. Create a movie")
        print("2. Delete a movie")
        print("3. Read movies")
        print("4. Update Movie")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the movie name: ")
            year = int(input("Enter the year: "))
            director_id = int(input("Enter the director ID: "))
            create_movie(name, year, director_id)
        elif choice == "2":
            read_movies()
            MovieId = int(input("Enter the MovieId: "))
            delete_movie(MovieId)
        elif choice == "3":
            read_movies()
        elif choice == "4":
            read_movies()
            movie_id = int(input("Please enter movie's id: "))
            title = input("Please enter movie title: ")
            year = int(input("Please enter movie year: "))
            director_id = int(input("Please enter movie director's id: "))
            update_movie(title, year, director_id, movie_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
