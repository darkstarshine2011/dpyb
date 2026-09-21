# d-py-b, a simple python database by darkstarshine2011

from datetime import datetime
from os import makedirs

def GetDataBaseName(DataBaseFile):
    if DataBaseFile[-8:] == ".dpyb.py":
        pass
    elif DataBaseFile[-5:] == ".dpyb":
        DataBaseFile = f"{DataBaseFile}.py"
    elif DataBaseFile[-3:] == ".py":
        DataBaseFile = f"{DataBaseFile[:-3]}.dpyb.py"
    else:
        DataBaseFile = f"{DataBaseFile}.dpyb.py"
    return DataBaseFile

def CreateBackup(DataBaseFile):
    makedirs("Backup", exist_ok=True)
    LoadForBackup = open(GetDataBaseName(DataBaseFile), "r")
    BackupFile = open(f"Backup/{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.dpyb.py.backup", "w+")
    BackupFile.write(LoadForBackup.read())
    BackupFile.close()
    LoadForBackup.close()

def CreateDataBase(DataBaseFile):
    """
    creates a new database on the file name
    """
    DataBaseFile = GetDataBaseName(DataBaseFile)

    File = open(DataBaseFile, "w+")
    File.write("# a d-py-b database file\n# d-py-b, a simple python database by darkstarshine2011\n\n# ---")
    File.close()

def AddTableToDataBase(DataBaseFile, TableName):
    """
    adds a new table into the database
    """
    CreateBackup(DataBaseFile)
    DBData = open(GetDataBaseName(DataBaseFile), "r").read()
    if f"{TableName} =" not in DBData and f"{TableName}=" not in DBData:
        DBFile = open(DataBaseFile, "a")
        DBFile.write(f"""\n\n# ---\n\n{TableName} = {{1:{{1:""}}}}""")


def AddRow(DataBaseFile, TableName, Rows):
    pass