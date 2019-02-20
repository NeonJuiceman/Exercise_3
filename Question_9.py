import arcpy


current_workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Q5GDB.gdb'

geometry_type = "POLYGON"

spatial_reference = arcpy.SpatialReference(102100)

featureClass = ['Town2']

arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')

createFC = [createFeatureClass(fc) for fc in featureClass]

in_table = 'Town2'
field_name = 'Town_Name'
field_type = 'TEXT'
gdb = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Q5GDB.gdb'

arcpy.AddField_management(in_table, field_name, field_type)

arcpy.env.workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Q5GDB.gdb'

arcpy.CreateDomain_management(gdb, 'Name1', 'Names of Towns', 'TEXT', 'CODED')

domDict = {'T':'Tigard', 'B':'Beaverton', 'C':'Corvallis', 'H':'Hillsboro', 'G':'Gresham'}

for code in domDict:
    arcpy.AddCodedValueToDomain_management(gdb, 'Name1', code, domDict[code])
