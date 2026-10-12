# Example 14 - An inventory system
# A small but complete inventory with add / sell / restock operations.

import dpyb

DB = "shop"
dpyb.CreateDataBase(DB)
dpyb.AddTableToDataBase(DB, "inventory")

# columns: 1 = name, 2 = price, 3 = stock
dpyb.AddColumn(DB, "inventory", 2)


def Find(ItemName):
    Table = dpyb.GetTable(DB, "inventory")
    for RowID in Table:
        if Table[RowID][1] == ItemName:
            return RowID
    return None


def AddItem(Name, Price, Stock=0):
    if Find(Name) is not None:
        print(f"'{Name}' already exists.")
        return
    Table = dpyb.GetTable(DB, "inventory")
    Row = (max(Table.keys()) + 1) if Table else 1
    if Row not in Table:
        dpyb.AddRow(DB, "inventory")
    dpyb.WriteData(DB, "inventory", Row, 1, Name)
    dpyb.WriteData(DB, "inventory", Row, 2, Price)
    dpyb.WriteData(DB, "inventory", Row, 3, Stock)


def Sell(Name, Quantity):
    Row = Find(Name)
    if Row is None:
        print(f"'{Name}' not found.")
        return
    Stock = dpyb.ReadData(DB, "inventory", Row, 3)
    if Stock < Quantity:
        print(f"Not enough stock for '{Name}' (have {Stock}).")
        return
    dpyb.WriteData(DB, "inventory", Row, 3, Stock - Quantity)


def Restock(Name, Quantity):
    Row = Find(Name)
    if Row is None:
        print(f"'{Name}' not found.")
        return
    Stock = dpyb.ReadData(DB, "inventory", Row, 3)
    dpyb.WriteData(DB, "inventory", Row, 3, Stock + Quantity)


def Show():
    Table = dpyb.GetTable(DB, "inventory")
    print(f"{'Item':<12} {'Price':>8} {'Stock':>8}")
    print("-" * 30)
    for RowID in Table:
        Row = Table[RowID]
        print(f"{Row[1]:<12} {Row[2]:>8} {Row[3]:>8}")


AddItem("Laptop", 1500, 10)
AddItem("Mouse", 25, 200)
AddItem("Keyboard", 80, 50)

Sell("Mouse", 5)
Restock("Laptop", 3)
Sell("Monitor", 1)   # not found

Show()





# # This example was written by DeepSeek.