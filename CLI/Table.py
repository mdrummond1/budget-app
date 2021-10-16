from Database import Database
from Constants import Queries
from Constants import TableNames

class BaseTable:
    def __init__(self, name, rows, db):
        self.name = name
        self.rows = rows
        self.__db = db

    def FindIndex(self, id):
        if len(self.rows) == 0:
            self.rows = self.Select()
        i = 0
        for row in rows:
            if row.id == id:
                break
            else:
                i += 1
        return i


    def Insert(self, row):
        self.rows.append(row)

    def Select(self):
        return db.SelectQuery(Queries['Select'] + f" * FROM {TableNames[self.name]}")

    def Update(self, id, newRow):
        row[self.FindIndex(id)] = newRow

    def Delete(self, id):
        rows.remove(self.FindIndex(id))
