# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", {1: "Ali", 2: 25})
dpyb.AddRow("mydb", "users", {1: "Sara", 2: 30})
dpyb.AddRow("mydb", "users", {1: "Reza", 2: 40})

Users = dpyb.GetTable("mydb", "users")

# Print every name and age
for RowID in Users:
    Name = Users[RowID][1]
    Age = Users[RowID][2]
    print(f"Row {RowID}: {Name}, age {Age}")