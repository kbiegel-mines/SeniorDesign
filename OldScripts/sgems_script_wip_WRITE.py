
#import numpy as np

# This script is to be called using RunScript in SGeMS
# The script will load a point set as hard data, create a new grid, then run sgsim
# on the grid with the input hard data.  The script will save the realizations
# into a single output file to be read in by another python sript (reading_control)
def writeSGEMSscript(path,scriptname,pointset,gridname,hardname,propname,numreal,gridfile,outfile):
    
    #path = 'C://Users/Ashton/Documents/School/SeniorDesign/wip/'
    #localpath = str('Z:/adit/My Documents/SeniorDesign/wip/') # for running this on a school computer
    fid = open(path+scriptname,'w') # replace localpath with path if running on SGeMS laptop
    #%% Importing current point set
    fid.write("import sgems \n")
    # Import point set
    fid.write("filename = '"+path+pointset+"'\n")
    fid.write('with open(filename) as f: \n')
    fid.write('    array = [[float(x) for x in line.split()] for line in f] \n')
    
    #nparray = np.array(array) # convert array to numpy array
    fid.write('f.close() \n')
    fid.write('samplx = [] \n')
    fid.write('samply = [] \n')
    fid.write('samplval = [] \n')
    fid.write('for i in range(len(array)): \n')
    fid.write('    samplx.append(array[i][0]) \n')
    fid.write('    samply.append(array[i][1]) \n')
    fid.write('    samplval.append(array[i][2]) \n')
    #real14_1 = nparray[:,0]
    #real14_2 = nparray[:,1]
    
    #%% RUNNING IN SGeMS
        
    # Load an existing project (necessary so that SGeMS has a 'place' to work)
    fid.write("sgems.execute('LoadProject C:/Users/Katherine/Documents/GitHub/SeniorDesign/project.prj') \n")
    
    # Initialize grid
    ###gridname = 'testgrid'    # Name of grid followed by grid dimensions
    fid.write("nx = '41' \n")
    fid.write("ny = '41' \n")
    fid.write("nz = '1' \n")
    fid.write("dx = '0.1' \n")
    fid.write("dy = '0.1' \n")
    fid.write("dz = '1.0' \n")
    fid.write("ox = '0' \n")
    fid.write("oy = '0' \n")
    fid.write("oz = '0' \n")
    fid.write("sgems.execute('NewCartesianGrid '+gridname+'::'+nx+'::'+ny+'::'+nz+'::'+dx+'::'+dy+'::'+dz+'::'+ox+'::'+oy+'::'+oz) \n")
    
    # Initialize other parameters
    ###hardname = 'iterate1' #property name to save hard data to
    ###propname = 'iterate319' #property name to base realization names off of
    ###numreal = '10' #number of realizations
    fid.write("varrange = '2' \n") # equal to half of the grid extent
    fid.write("searchelips = str(2*int(varrange)) \n") # equal to the whole grid extent
    
    # Assign hard data to grid
    fid.write("sgems.set_property(gridname,hardname,samplval) \n")
    
    # Run SGSIM
    fid.write("sgems.execute('RunGeostatAlgorithm  sgsim::/GeostatParamUtils/XML::<parameters>  <algorithm name=\"sgsim\" />     <Grid_Name value=\"'+gridname+'\" />     <Property_Name  value=\"'+propname+'\" />     <Nb_Realizations  value=\"'+numreal+'\" />     <Seed  value=\"14071789\" />     <Kriging_Type  value=\"Simple Kriging (SK)\"  />     <Variogram  nugget=\"0\" structures_count=\"1\"  >    <structure_1  contribution=\"1\"  type=\"Spherical\"   >       <ranges max=\"'+varrange+'\"  medium=\"'+varrange+'\"  min=\"'+varrange+'\"   />       <angles x=\"0\"  y=\"0\"  z=\"0\"   />    </structure_1>  </Variogram>     <Assign_Hard_Data  value=\"1\"  />      <Hard_Data  grid=\"'+gridname+'\"  property=\"'+hardname+'\"  />      <Max_Conditioning_Data  value=\"12\" />      <Search_Ellipsoid  value=\"'+searchelips+' '+searchelips+' '+searchelips+' 0 0 0\" />     <AdvancedSearch  use_advanced_search=\"0\"></AdvancedSearch>    <Use_Target_Histogram  value=\"0\"  />     </parameters>  \') \n")
    
    #%% SAVING OUTPUTS
    # Save simulation grid coordinates
    fid.write("gridfile = '"+path+gridfile+"'\n")
    
    fid.write("separator = ' ' \n")
    
    fid.write("x = sgems.get_property(gridname,\"_X_\") \n")
    
    fid.write("y = sgems.get_property(gridname,\"_Y_\") \n")
    
    fid.write("fid1 = open(gridfile,'w') \n")
    
    fid.write("for i,j in zip(x,y) : fid1.write(str(i)+separator+str(j)+'\\n') \n")
    
    fid.write("fid1.close() \n")
    
    # Loop through all realizations and save to a list.
    fid.write("real_319 = [] \n")
    fid.write("for i in range(int(numreal)): \n")
    fid.write("    real_319.append(sgems.get_property(gridname,propname+'__real%d' % (i))) \n")
    # real_319[0] = realization 0, real_319[0][i] = cell i of realization 0
    
    # To save directly -> pretty cumbersome
    #sgems.execute('SaveGeostatGrid  gauss::C:/Users/Ashton/Documents/School/SeniorDesign/project_3-2.prj/testing::csv::0::14__real0::14__real1')
    
    # Save realizations to a single file
    fid.write("outfile = '"+path+outfile+"'\n")
    fid.write("f = open(outfile,'w') \n")
    fid.write("for i in range(len(real_319[0])): \n")
    fid.write("    for j in range(len(real_319)): \n")
    fid.write("        f.write(str(real_319[j][i])) \n")
    fid.write("        f.write(' ') \n")
    fid.write("    f.write(' \\n') \n")
    fid.write("f.close() \n")
    
    fid.close()
    
# Example function-run command
# writeSGEMSscript('sgems_script_test.py','Sample.txt','testgrid320','hardtest320','simtest320','10','testgrid320_out.txt','test320_out.txt')