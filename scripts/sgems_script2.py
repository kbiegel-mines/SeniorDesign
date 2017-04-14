import sgems 
filename = 'C:/Users/Katherine/Documents/GitHub/SeniorDesign/inputs/sgems_inputs_1.txt'
with open(filename) as f: 
    for x in range(5): 
        next(f) 
    array = [[float(x) for x in line.split()] for line in f] 
f.close() 
samplx = [] 
samply = [] 
samplval = [] 
for i in range(len(array)): 
    samplx.append(array[i][0]) 
    samply.append(array[i][1]) 
    samplval.append(array[i][2]) 
sgems.execute('LoadProject C:/Users/Katherine/Documents/GitHub/SeniorDesign/project.prj') 
nx = '41' 
ny = '41' 
nz = '1' 
dx = '0.1' 
dy = '0.1' 
dz = '1.0' 
ox = '0' 
oy = '0' 
oz = '0' 
sgems.execute('NewCartesianGrid gridxy::'+nx+'::'+ny+'::'+nz+'::'+dx+'::'+dy+'::'+dz+'::'+ox+'::'+oy+'::'+oz) 
varrange = '2' 
searchelips = str(2*int(varrange)) 
sgems.set_property('gridxy','hardtest2',samplval) 
sgems.execute('RunGeostatAlgorithm  sgsim::/GeostatParamUtils/XML::<parameters>  <algorithm name="sgsim" />     <Grid_Name value="gridxy" />     <Property_Name  value="simtest2" />     <Nb_Realizations  value="10" />     <Seed  value="14071789" />     <Kriging_Type  value="Simple Kriging (SK)"  />     <Variogram  nugget="0" structures_count="1"  >    <structure_1  contribution="1"  type="Spherical"   >       <ranges max="'+varrange+'"  medium="'+varrange+'"  min="'+varrange+'"   />       <angles x="0"  y="0"  z="0"   />    </structure_1>  </Variogram>     <Assign_Hard_Data  value="1"  />      <Hard_Data  grid="gridxy"  property="hardtest2"  />      <Max_Conditioning_Data  value="12" />      <Search_Ellipsoid  value="'+searchelips+' '+searchelips+' '+searchelips+' 0 0 0" />     <AdvancedSearch  use_advanced_search="0"></AdvancedSearch>    <Use_Target_Histogram  value="0"  />     </parameters>  ') 
gridfile = 'C:/Users/Katherine/Documents/GitHub/SeniorDesign/gridxy.txt'
separator = ' ' 
x = sgems.get_property("gridxy","_X_") 
y = sgems.get_property("gridxy","_Y_") 
fid1 = open(gridfile,'w') 
for i,j in zip(x,y) : fid1.write(str(i)+separator+str(j)+'\n') 
fid1.close() 
real_319 = [] 
for i in range(int(10)): 
    real_319.append(sgems.get_property("gridxy","simtest2__real%d" % (i))) 
outfile = 'C:/Users/Katherine/Documents/GitHub/SeniorDesign/outputs/testout2.txt'
f = open(outfile,'w') 
for i in range(len(real_319[0])): 
    for j in range(len(real_319)): 
        f.write(str(real_319[j][i])) 
        f.write(' ') 
    f.write(' \n') 
f.close() 
