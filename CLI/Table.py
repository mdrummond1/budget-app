from Database import Database
from Constants import Queries
from Constants import TableNames

#TODO: create types for each table row
# table types
# class TableRow:
#     def __init__(self, *data):
#         self.data = data
#         pass


# class Table:
#     def __init__(self, name: str, db: Database):
#         self.name: str = name
#         self.__db: Database = db

#     def FindIndex(self, id) -> int:
#         rows = self.Select(self)
#         i = 0
#         for row in rows:
#             if row.id == id:
#                 break
#             else:
#                 i += 1
#         return i


#     def Insert(self, obj: TableRow):
#         vals = ""
#         for d in obj.data:
#             vals += d

#         self.__db.ChangeQuery(Queries['Insert' + f" INTO {self.name} VALUES({vals})"])


#     def Select(self):
#         return self.__db.SelectQuery(Queries['Select'] + f" * FROM {TableNames[self.name]}")

#     def Update(self, id, newRow):
#         return self.__db.ChangeQuery(Queries['Update'] + f" TABLE {TableNames[self.name]} ")
#         row[self.FindIndex(id)] = newRow

#     def Delete(self, id):
#         rows.remove(self.FindIndex(id))
