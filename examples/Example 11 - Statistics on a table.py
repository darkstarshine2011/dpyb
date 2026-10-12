# Example 11 - Statistics on a table
# Compute simple stats using plain Python on top of dpyb.

import dpyb

dpyb.CreateDataBase("mydb")
dpyb.AddTableToDataBase("mydb", "sales")

Data = [120, 340, 80, 500, 210, 150, 400]

dpyb.AddRow("mydb", "sales", len(Data) - 1)

for i, Amount in enumerate(Data, start=1):
    dpyb.WriteData("mydb", "sales", i, 1, Amount)

Sales = dpyb.GetTable("mydb", "sales")

Values = [Sales[Row][1] for Row in Sales]

print(f"Count:   {len(Values)}")
print(f"Sum:     {sum(Values)}")
print(f"Average: {sum(Values) / len(Values):.2f}")
print(f"Min:     {min(Values)}")
print(f"Max:     {max(Values)}")

# Count sales above a threshold
Threshold = 200
Above = [v for v in Values if v > Threshold]
print(f"Above {Threshold}: {len(Above)} entries")





# # This example was written by DeepSeek.