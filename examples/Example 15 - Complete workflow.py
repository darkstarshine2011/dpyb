# Example 15 - Complete workflow
# A tour through the entire API, end to end.

import dpyb

# 1. Create a database
dpyb.CreateDataBase("mydb")

# 2. Add tables
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddTableToDataBase("mydb", "posts")

# 3. Grow the "users" table
dpyb.AddRow("mydb", "users", 2)      # 3 rows total
dpyb.AddColumn("mydb", "users", 2)   # 3 columns total

# 4. Fill users
Users = [
    ("Ali",  25, "Tehran"),
    ("Sara", 30, "Shiraz"),
    ("Reza", 40, "Mashhad"),
]
for i, (Name, Age, City) in enumerate(Users, start=1):
    dpyb.WriteData("mydb", "users", i, 1, Name)
    dpyb.WriteData("mydb", "users", i, 2, Age)
    dpyb.WriteData("mydb", "users", i, 3, City)

# 5. Grow and fill "posts"
dpyb.AddRow("mydb", "posts", 3)      # 4 rows total
dpyb.AddColumn("mydb", "posts", 1)   # 2 columns total

Posts = [
    (1, "Hello world"),
    (1, "Another post by Ali"),
    (2, "Sara's first post"),
    (3, "Reza is here"),
]
for i, (AuthorID, Title) in enumerate(Posts, start=1):
    dpyb.WriteData("mydb", "posts", i, 1, AuthorID)
    dpyb.WriteData("mydb", "posts", i, 2, Title)

# 6. Read everything back
print("Tables:", dpyb.ListTables("mydb"))

UsersTable = dpyb.GetTable("mydb", "users")
PostsTable = dpyb.GetTable("mydb", "posts")

print("\nUsers:")
for RowID in UsersTable:
    Row = UsersTable[RowID]
    print(f"  [{RowID}] {Row[1]} ({Row[2]}) - {Row[3]}")

print("\nPosts:")
for RowID in PostsTable:
    Row = PostsTable[RowID]
    Author = UsersTable[Row[1]][1] if Row[1] in UsersTable else "unknown"
    print(f"  [{RowID}] by {Author}: {Row[2]}")

# 7. Update: Ali moved to Karaj
dpyb.WriteData("mydb", "users", 1, 3, "Karaj")
print("\nAli's new city:", dpyb.ReadData("mydb", "users", 1, 3))

# 8. Delete: remove Reza from users
dpyb.DeleteRow("mydb", "users", 3)
print("Users after deletion:", len(dpyb.GetTable("mydb", "users")))

# 9. Delete a column from every user
dpyb.DeleteColumn("mydb", "users", 2)   # remove the "age" column
print("Row 1 after removing age column:", dpyb.GetTable("mydb", "users")[1])

# 10. Delete a table
dpyb.DeleteTable("mydb", "posts")
print("Remaining tables:", dpyb.ListTables("mydb"))





# # This example was written by DeepSeek.