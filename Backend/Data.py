import sqlite3

def InitialiseTables():
    with sqlite3.connect("./Backend/Data.db") as db:
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS User(
                UserID integer,
                Firstname varchar(20),
                Lastname varchar(20),
                Username text UNIQUE,
                Email text UNIQUE,
                Password text,
                Primary key(UserID));
            """
        cursor.execute(sql)

class Server():
    def __init__(self):
        self.Username = ""
        self.FName = ""
        self.LName = ""
        self.Email = ""
        self.Password = ""
        self.UserID = 0
    
    def CheckPassword(self, Password, Username):
        try:
            Values = (Username,)
            with sqlite3.connect("./Backend/Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT Password FROM User
                         WHERE Username = ?;
                    """
                cursor.execute(sql, Values)
                result, = cursor.fetchone()
                print(result)
                if result == Password:
                    return True
                else:
                    return False
        except:
            return False