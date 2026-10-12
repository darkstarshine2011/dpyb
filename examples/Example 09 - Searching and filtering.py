# Example 09 - Searching and filtering
# Find rows that match a condition.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")

Data = [
    ("Ali",    25, "Tehran"),
    ("Sara",   30, "Shiraz"),
    ("Reza",   40, "Mashhad"),
    ("Mina",   22, "Tehran"),
    ("Omid",   35, "Isfahan"),
]

dpyb.AddRow("mydb", "users", len(Data) - 1)
dpyb.AddColumn("mydb", "users", 2)

for i, (Name, Age, City) in enumerate(Data, start=1):
    dpyb.WriteData("mydb", "users", i, 1, Name)
    dpyb.WriteData("mydb", "users", i, 2, Age)
    dpyb.WriteData("mydb", "users", i, 3, City)

Users = dpyb.GetTable("mydb", "users")

# Find users older than 28
print("Users older than 28:")
for RowID in Users:
    if Users[RowID][2] > 28:
        print(f"  {Users[RowID][1]} ({Users[RowID][2]})")

# Find users from Tehran
print("\nUsers from Tehran:")
for RowID in Users:
    if Users[RowID][3] == "Tehran":
        print(f"  {Users[RowID][1]}")
        




# # This example was written by DeepSeek.