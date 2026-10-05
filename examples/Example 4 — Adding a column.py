# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", {1: "Ali", 2: 25})
dpyb.AddRow("mydb", "users", {1: "Sara", 2: 30})

# Add a new column with a default value
dpyb.AddColumn("mydb", "users", "unknown")

# Every row now has a 3rd column:
# {1: {1: "Ali", 2: 25, 3: "unknown"},
#  2: {1: "Sara", 2: 30, 3: "unknown"}}