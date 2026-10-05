# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddTableToDataBase("mydb", "posts")
dpyb.AddRow("mydb", "users", {1: "Ali"})

# List all tables
print(dpyb.ListTables("mydb"))  # ["users", "posts"]

# Get the whole "users" table as a dict
Users = dpyb.GetTable("mydb", "users")
print(Users)  # {1: {1: "Ali"}}