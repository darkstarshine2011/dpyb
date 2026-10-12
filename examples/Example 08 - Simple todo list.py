# Example 08 - Simple todo list
# A tiny command-line todo app using dpyb.

import dpyb

DB = "todo"
dpyb.CreateDataBase(DB)
dpyb.AddTableToDataBase(DB, "tasks")

# columns: 1 = title, 2 = done (True/False)
dpyb.AddColumn(DB, "tasks", 1)


def AddTask(Title):
    Table = dpyb.GetTable(DB, "tasks")
    Row = (max(Table.keys()) + 1) if Table else 1
    # If the table is empty, ensure the row exists
    if Row not in Table:
        dpyb.AddRow(DB, "tasks")
    dpyb.WriteData(DB, "tasks", Row, 1, Title)
    dpyb.WriteData(DB, "tasks", Row, 2, False)


def MarkDone(Row):
    dpyb.WriteData(DB, "tasks", Row, 2, True)


def ShowTasks():
    Table = dpyb.GetTable(DB, "tasks")
    for RowID in Table:
        Title = Table[RowID][1]
        Done = Table[RowID][2]
        Box = "[x]" if Done else "[ ]"
        print(f"{Box} {RowID}: {Title}")


AddTask("Buy milk")
AddTask("Walk the dog")
AddTask("Finish the report")
MarkDone(1)

ShowTasks()
# [x] 1: Buy milk
# [ ] 2: Walk the dog
# [ ] 3: Finish the report





# # This example was written by DeepSeek.