# Example 10 - Contact book
# A slightly more complete app with add, search, and delete.

import dpyb

DB = "contacts"
dpyb.CreateDataBase(DB)
dpyb.AddTableToDataBase(DB, "people")

# columns: 1 = name, 2 = phone, 3 = email
dpyb.AddColumn(DB, "people", 2)


def AddContact(Name, Phone, Email):
    Table = dpyb.GetTable(DB, "people")
    Row = (max(Table.keys()) + 1) if Table else 1
    if Row not in Table:
        dpyb.AddRow(DB, "people")
    dpyb.WriteData(DB, "people", Row, 1, Name)
    dpyb.WriteData(DB, "people", Row, 2, Phone)
    dpyb.WriteData(DB, "people", Row, 3, Email)


def FindContact(Name):
    Table = dpyb.GetTable(DB, "people")
    for RowID in Table:
        if Table[RowID][1].lower() == Name.lower():
            return RowID, Table[RowID]
    return None, None


def DeleteContact(Name):
    RowID, _ = FindContact(Name)
    if RowID is not None:
        dpyb.DeleteRow(DB, "people", RowID)


def ListAll():
    Table = dpyb.GetTable(DB, "people")
    for RowID in Table:
        Row = Table[RowID]
        print(f"{Row[1]:<10} {Row[2]:<15} {Row[3]}")


AddContact("Ali",  "0912...", "ali@example.com")
AddContact("Sara", "0913...", "sara@example.com")
AddContact("Reza", "0914...", "reza@example.com")

print("All contacts:")
ListAll()

print("\nLooking for Sara:")
RowID, Row = FindContact("Sara")
print(f"  Found at row {RowID}: {Row}")

DeleteContact("Ali")
print("\nAfter deleting Ali:")
ListAll()





# # This example was written by DeepSeek.