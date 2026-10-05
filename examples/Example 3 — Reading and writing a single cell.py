# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", {1: "Ali", 2: 25})

# Read a cell: row 1, column 1
Name = dpyb.ReadData("mydb", "users", 1, 1)
print(Name)  # "Ali"

# Write a new value into row 1, column 2
dpyb.WriteData("mydb", "users", 1, 2, 26)

print(dpyb.ReadData("mydb", "users", 1, 2))  # 26