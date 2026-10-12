# Example 05 - Multiple tables
# A single database can hold many tables.

import dpyb

dpyb.CreateDataBase("mydb")

dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddTableToDataBase("mydb", "posts")
dpyb.AddTableToDataBase("mydb", "comments")

dpyb.AddRow("mydb", "users", 3)
dpyb.AddRow("mydb", "posts", 5)
dpyb.AddRow("mydb", "comments", 10)

print(dpyb.ListTables("mydb"))
# ["users", "posts", "comments"]

# Each table is independent
print(len(dpyb.GetTable("mydb", "users")))      # 4 rows
print(len(dpyb.GetTable("mydb", "posts")))      # 6 rows
print(len(dpyb.GetTable("mydb", "comments")))   # 11 rows





# # This example was written by DeepSeek.