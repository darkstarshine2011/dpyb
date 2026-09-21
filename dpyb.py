# d-py-b, a simple python database by darkstarshine2011

def CreateDataBase(DataBaseFile):
    """
    creates a new database on the file name
    """
    if DataBaseFile[-8:] == ".dpyb.py":
        pass
    elif DataBaseFile[-5:] == ".dpyb":
        DataBaseFile = f"{DataBaseFile}.py"
    elif DataBaseFile[-3:] == ".py":
        DataBaseFile = f"{DataBaseFile[:-3]}.dpyb.py"
    else:
        DataBaseFile = f"{DataBaseFile}.dpyb.py"

    File = open(DataBaseFile, "w")
    File.write("# a d-py-b database file\n# d-py-b, a simple python database by darkstarshine2011\n\n")
    File.close()

def AddTableToDataBase(DataBaseFile, TableName):
    pass


