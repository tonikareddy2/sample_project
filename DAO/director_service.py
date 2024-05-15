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

    def update_Director(self, name, DirectorID):
        try:
            self.cursor.execute(
                """
            Update Movies
            Set name = ?
            where DirectorId = ?
            """,
                (name, DirectorID),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
