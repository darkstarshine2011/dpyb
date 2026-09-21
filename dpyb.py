# d-py-b, a simple python database by darkstarshine2011

from datetime import now

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
    LoadForBackup = open(GetDataBaseName(DataBaseFile), "r")
    BackupFile = open(f"Backup/{now()}.dpyb.py.backup", "w")
    BackupFile.write(LoadForBackup)
    BackupFile.close()
    LoadForBackup.close()

def CreateDataBase(DataBaseFile):
    """
    creates a new database on the file name
    """
    DataBaseFile = GetDataBaseName(DataBaseFile)

    File = open(DataBaseFile, "w")
    File.write("# a d-py-b database file\n# d-py-b, a simple python database by darkstarshine2011\n\n---")
    File.close()

def AddTableToDataBase(DataBaseFile, TableName):
    CreateBackup(DataBaseFile)
    DBData = open(DataBaseFile, "r")
    if f"{TableName} =" not in DBData or f"{TableName}=" not in DBData:
        DBFile = open(DataBaseFile, "a")
        DBFile.write(f"""{DBData}\n\n---\n\n{TableName} = \{1:\{1:""}}""")
    DBData.close()
