# Example 04 - Iterating over a table
# How to loop through every row and every cell.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", 2)
dpyb.AddColumn("mydb", "users", 2)

dpyb.WriteData("mydb", "users", 1, 1, "Ali")
dpyb.WriteData("mydb", "users", 1, 2, 25)
dpyb.WriteData("mydb", "users", 1, 3, "Tehran")

dpyb.WriteData("mydb", "users", 2, 1, "Sara")
dpyb.WriteData("mydb", "users", 2, 2, 30)
dpyb.WriteData("mydb", "users", 2, 3, "Shiraz")

dpyb.WriteData("mydb", "users", 3, 1, "Reza")
dpyb.WriteData("mydb", "users", 3, 2, 40)
dpyb.WriteData("mydb", "users", 3, 3, "Mashhad")

Users = dpyb.GetTable("mydb", "users")

# Loop through rows
for RowID in Users:
    Name = Users[RowID][1]
    Age = Users[RowID][2]
    City = Users[RowID][3]
    print(f"Row {RowID}: {Name}, {Age} years old, from {City}")

# Output:
# Row 1: Ali, 25 years old, from Tehran
# Row 2: Sara, 30 years old, from Shiraz
# Row 3: Reza, 40 years old, from Mashhad





# # This example was written by DeepSeek.