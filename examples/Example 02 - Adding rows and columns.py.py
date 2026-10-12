# Example 02 - Adding rows and columns
# How AddRow and AddColumn work.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")

# Start: 1 row, 1 column
print(dpyb.GetTable("mydb", "users"))
# {1: {1: ''}}

# Add 4 more rows (total: 5 rows)
dpyb.AddRow("mydb", "users", 4)

# Add 2 more columns (total: 3 columns)
dpyb.AddColumn("mydb", "users", 2)

print(dpyb.GetTable("mydb", "users"))
# {
#   1: {1: '', 2: '', 3: ''},
#   2: {1: '', 2: '', 3: ''},
#   3: {1: '', 2: '', 3: ''},
#   4: {1: '', 2: '', 3: ''},
#   5: {1: '', 2: '', 3: ''},
# }

# Key point: every row always has the same columns.
# New rows inherit existing columns. New columns are added to every row.





# # This example was written by DeepSeek.