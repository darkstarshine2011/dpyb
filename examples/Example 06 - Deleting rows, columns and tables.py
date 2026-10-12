# Example 06 - Deleting rows, columns and tables
# Removing data from a database.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", 4)
dpyb.AddColumn("mydb", "users", 3)

# Delete a single row
dpyb.DeleteRow("mydb", "users", 2)
print(len(dpyb.GetTable("mydb", "users")))   # 4 rows (was 5)

# Delete a single column from every row
dpyb.DeleteColumn("mydb", "users", 1)
print(dpyb.GetTable("mydb", "users"))
# every row now has columns 2, 3, 4

# Delete the entire table
dpyb.DeleteTable("mydb", "users")
print(dpyb.ListTables("mydb"))   # []





# # This example was written by DeepSeek.