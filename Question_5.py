import arcpy

out_folder_path = r'C:\Users\NeonJuiceman\Desktop\Exercise 3'
out_name = 'Q5GDB_1.gdb'

arcpy.CreateFileGDB_management(out_folder_path, out_name)

print('All Done')

current_workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Q5GDB.gdb'

geometry_type = "POLYGON"

spatial_reference = arcpy.SpatialReference(102100)

featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']

arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]


