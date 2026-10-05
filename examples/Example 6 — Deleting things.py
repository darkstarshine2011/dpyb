# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", {1: "Ali", 2: 25, 3: "Tehran"})
dpyb.AddRow("mydb", "users", {1: "Sara", 2: 30, 3: "Shiraz"})

# Delete row 1
dpyb.DeleteRow("mydb", "users", 1)

# Delete column 3 from every row
dpyb.DeleteColumn("mydb", "users", 3)

# Delete the entire "users" table
dpyb.DeleteTable("mydb", "users")