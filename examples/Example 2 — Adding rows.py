# Written by DeepSeek
import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")

# Add a row with three columns
dpyb.AddRow("mydb", "users", {1: "Ali", 2: 25, 3: "Tehran"})

# Add another row
dpyb.AddRow("mydb", "users", {1: "Sara", 2: 30, 3: "Shiraz"})

# The table now looks like:
# {1: {1: "Ali", 2: 25, 3: "Tehran"},
#  2: {1: "Sara", 2: 30, 3: "Shiraz"}}