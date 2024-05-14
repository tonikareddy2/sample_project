import pyodbc

server_name = "DESKTOP-P8QAI2N\SQLEXPRESS"
database_name = "HexawareMovieDB"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
print(conn_str)


class DBconnection:
    def __init__(self):
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
