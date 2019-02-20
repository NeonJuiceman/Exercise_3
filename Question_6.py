import arcpy

arcpy.env.workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb'

arcpy.overwriteOutput = True

in_table = 'CallsforService'
field_name = 'Crime_Explanation'
field_type = 'TEXT'

arcpy.AddField_management(in_table, field_name, field_type)

fc = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\CallsforService'
fields = ['CFSType', 'Crime_Explanation']

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if row[0] == 'Burglary Call':
            row[1] = 'This is a burglary'
        cursor.updateRow(row)
        del cursor
        print('All Complete')

