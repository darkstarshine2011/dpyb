# Written by DeepSeek
import dpyb

# Create a new database file
dpyb.CreateDataBase("mydb")

# Add two tables
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddTableToDataBase("mydb", "posts")