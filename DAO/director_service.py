from Util.DBconn import DBconnection


class DirectorService(DBconnection):
    def view_directors(self):
        try:
            self.cursor.execute("SELECT * FROM Directors")
            for row in self.cursor:
                print(row)
        except Exception as e:
            print(e)
