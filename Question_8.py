import arcpy

arcpy.env.workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3_New.gdb'

arcpy.env.overwriteOutput = True

fc = r'C:\Users\NeonJuiceman\Desktop\Exercise 3_New.gdb\CallsforService'

printCount = arcpy.GetCount_management(fc)

print(str(printCount))

