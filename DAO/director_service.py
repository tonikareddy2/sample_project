from Util.DBconn import DBconnection
from abc import ABC, abstractmethod


# @-decorators
class IDirectorService(ABC):
    @abstractmethod
    def view_directors(self):
        pass

    @abstractmethod
    def add_director(self, Director):
        pass

    @abstractmethod
    def read_director_by_id(self, DirectorID):
        pass


class DirectorNotFoundError(Exception):
    def __init__(self, director_id):
        super().__init__(f"Director with {director_id} is not found")


class DirectorService(IDirectorService, DBconnection):
    def view_directors(self):
        try:
            self.cursor.execute("SELECT * FROM Directors")
            for row in self.cursor:
                print(row)
        except Exception as e:
            print(e)

    def add_director(self, Director):
        try:
            self.cursor.execute(
                "INSERT INTO Directors (Name) VALUES (?)", (Director.name,)
            )
            self.conn.commit()
            print("Director added successfully.")
        except Exception as e:
            print(e)

    def read_director_by_id(self, DirectorID):
        try:
            self.cursor.execute(
                "Select * from Directors where DirectorId=?", (DirectorID,)
            )

            directors = self.cursor.fetchall()
            if len(directors) == 0:
                raise DirectorNotFoundError(DirectorID)
            else:
                print(directors)  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
