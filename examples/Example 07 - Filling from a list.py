# Example 07 - Filling from a list
# Populate a table from a Python list.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "products")

Data = [
    ("Laptop",  1500, 10),
    ("Mouse",     25, 200),
    ("Keyboard",  80, 50),
    ("Monitor",  300, 15),
    ("Webcam",    60, 30),
]

# 1 initial row + (len(Data) - 1) new rows
dpyb.AddRow("mydb", "products", len(Data) - 1)

# 1 initial column + 2 new columns
dpyb.AddColumn("mydb", "products", 2)

# Fill the table
for i, (Name, Price, Stock) in enumerate(Data, start=1):
    dpyb.WriteData("mydb", "products", i, 1, Name)
    dpyb.WriteData("mydb", "products", i, 2, Price)
    dpyb.WriteData("mydb", "products", i, 3, Stock)

for RowID in dpyb.GetTable("mydb", "products"):
    Row = dpyb.GetTable("mydb", "products")[RowID]
    print(f"{Row[1]:<10} ${Row[2]:>5}  stock: {Row[3]}")
    




# # This example was written by DeepSeek.