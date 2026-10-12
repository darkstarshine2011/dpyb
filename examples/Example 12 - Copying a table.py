# Example 12 - Copying a table
# Duplicate a table inside the same database.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "original")
dpyb.AddRow("mydb", "original", 2)
dpyb.AddColumn("mydb", "original", 1)

dpyb.WriteData("mydb", "original", 1, 1, "A")
dpyb.WriteData("mydb", "original", 1, 2, "B")
dpyb.WriteData("mydb", "original", 2, 1, "C")
dpyb.WriteData("mydb", "original", 2, 2, "D")
dpyb.WriteData("mydb", "original", 3, 1, "E")
dpyb.WriteData("mydb", "original", 3, 2, "F")

Source = dpyb.GetTable("mydb", "original")

# Create a new table
dpyb.AddTableToDataBase("mydb", "copy")

# Clear it and rebuild
dpyb.DeleteTable("mydb", "copy")
dpyb.AddTableToDataBase("mydb", "copy")

# Copy row by row
Rows = len(Source)
Cols = len(next(iter(Source.values()))) if Source else 0

dpyb.AddRow("mydb", "copy", Rows - 1)
dpyb.AddColumn("mydb", "copy", Cols - 1)

for RowID in Source:
    for ColID in Source[RowID]:
        dpyb.WriteData("mydb", "copy", RowID, ColID, Source[RowID][ColID])

print(dpyb.GetTable("mydb", "copy"))
# Same content as "original"





# # This example was written by DeepSeek.