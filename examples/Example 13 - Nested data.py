# Example 13 - Nested data
# dpyb values can be any Python literal, including lists and dicts.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "users")
dpyb.AddRow("mydb", "users", 1)
dpyb.AddColumn("mydb", "users", 2)

# Column 1: name (str)
dpyb.WriteData("mydb", "users", 1, 1, "Ali")

# Column 2: tags (list)
dpyb.WriteData("mydb", "users", 1, 2, ["admin", "developer", "python"])

# Column 3: metadata (dict)
dpyb.WriteData("mydb", "users", 1, 3, {
    "signup_year": 2024,
    "country": "Iran",
    "active": True,
})

# Column 2 of the second row: another list
dpyb.WriteData("mydb", "users", 2, 1, "Sara")
dpyb.WriteData("mydb", "users", 2, 2, ["moderator"])
dpyb.WriteData("mydb", "users", 2, 3, {"signup_year": 2025, "country": "Iran", "active": False})

# Read nested data back
Users = dpyb.GetTable("mydb", "users")

print(Users[1][2])            # ["admin", "developer", "python"]
print(Users[1][3]["country"]) # "Iran"

# Loop over nested lists
for RowID in Users:
    print(f"{Users[RowID][1]}: {', '.join(Users[RowID][2])}")
    




# # This example was written by DeepSeek.