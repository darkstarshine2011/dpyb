# Example 03 - Reading and writing cells
# Working with individual cells.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", 2)
dpyb.AddColumn("mydb", "users", 2)

# Fill row 1
dpyb.WriteData("mydb", "users", 1, 1, "Ali")
dpyb.WriteData("mydb", "users", 1, 2, 25)
dpyb.WriteData("mydb", "users", 1, 3, "Tehran")

# Fill row 2
dpyb.WriteData("mydb", "users", 2, 1, "Sara")
dpyb.WriteData("mydb", "users", 2, 2, 30)
dpyb.WriteData("mydb", "users", 2, 3, "Shiraz")

# Read some cells
print(dpyb.ReadData("mydb", "users", 1, 1))   # "Ali"
print(dpyb.ReadData("mydb", "users", 2, 3))   # "Shiraz"

# Update a cell
dpyb.WriteData("mydb", "users", 1, 2, 26)
print(dpyb.ReadData("mydb", "users", 1, 2))   # 26




# # This example was written by DeepSeek.