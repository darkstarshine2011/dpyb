# Example 01 - Getting started
# The absolute basics of dpyb.

import dpyb

# Create a brand new database file called "mydb.dpyb.py"
dpyb.CreateDataBase("mydb")

# Add a table called "users"
dpyb.AddTableToDataBase("mydb", "users")

# A new table always starts with 1 row and 1 column.
print(dpyb.GetTable("mydb", "users"))
# {1: {1: ''}}

# Write something into the very first cell
dpyb.WriteData("mydb", "users", 1, 1, "Hello, dpyb!")

# Read it back
print(dpyb.ReadData("mydb", "users", 1, 1))
# "Hello, dpyb!"

# List all tables
print(dpyb.ListTables("mydb"))
# ["users"]





# # This example was written by DeepSeek.