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
                if result == Password:
                    return True
                else:
                    return False
        except:
            return False
        
    def FindUserID(self, Field):
        try:
            Values = (Field, Field)
            with sqlite3.connect("./Backend/Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT UserID FROM User
                        WHERE Username = ? OR Email = ?;
                     """
                cursor.execute(sql, Values)
                result, = cursor.fetchone()
                return result
        except:
            return False

    def LogAssociate(self, UserID):
        try:
            Values = (UserID,)
            with sqlite3.connect("./Backend/Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT * FROM User
                        WHERE UserID = ?;
                    """
                cursor.execute(sql, Values)
                result, = cursor.fetchall()
                self.UserID = result[0]
                self.FName = result[1]
                self.LName = result[2]
                self.Username = result[3]
                self.Email = result[4]
                self.Password = result[5]
        except:
            return False

    def Login(self, Username, Password):
        UserID = self.FindUserID(Username)
        if UserID != False:
            if self.CheckPassword(Password, Username):
                self.LogAssociate(UserID)
                return True
            else:
                return False
        else:
            return False
        
    def CreateAccount(self, FName, LName, Username, Email, Password):
        try:
            Values = (FName, LName, Username, Email, Password)
            with sqlite3.connect("./Backend/Data.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO User(Firstname, Lastname, Username, Email, Password)
                            Values(?, ?, ?, ?, ?)
                        """
                cursor.execute(sql, Values)
                return True
        except:
            return False
