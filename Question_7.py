import arcpy

arcpy.env.workspace = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb'

arcpy.env.overwriteOutput = True

featureclass01 = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\General_Offense'

arcpy.MakeFeatureLayer_management(featureclass01,'GeneralOffense_lyr')

arcpy.SelectLayerByAttribute_management('GeneralOffense_lyr', 'NEW_SELECTION', 'x_rand > 10')

arcpy.CopyFeatures_management('GeneralOffense_lyr', r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\New_Selection')



