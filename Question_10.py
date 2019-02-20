import arcpy

target_features = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\Tracts'
join_features = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\General_Offense'
out_feature_class = r'C:\Users\NeonJuiceman\Desktop\Exercise 3\Exercise 3.gdb\Tracts_Join'

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)