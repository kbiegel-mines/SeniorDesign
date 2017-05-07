import sgems 
filename = "C://Users/Katherine/Documents/GitHub/SeniorDesign/current/current/sgems_inputs.txt"
with open(filename) as f: 
    for x in range(5): 
        next(f) 
    array = [[float(x) for x in line.split()] for line in f] 
f.close() 
samplx = [] 
samply = [] 
samplz = [] 
samplval = [] 
for i in range(len(array)): 
    samplx.append(array[i][0]) 
    samply.append(array[i][1]) 
    samplz.append(0) 
    samplval.append(array[i][2]) 
nx = '41' 
ny = '41' 
nz = '1' 
dx = '0.1' 
dy = '0.1' 
dz = '1.0' 
ox = '0' 
oy = '0' 
oz = '0' 
sgems.execute('NewCartesianGrid gridxy0::'+nx+'::'+ny+'::'+nz+'::'+dx+'::'+dy+'::'+dz+'::'+ox+'::'+oy+'::'+oz) 
varrange = '2' 
searchelips = str(2*int(varrange)) 
sgems.new_point_set('pointset0',samplx,samply,samplz) 
sgems.set_property('pointset0','hardtest0',samplval) 
sgems.execute('RunGeostatAlgorithm  sgsim::/GeostatParamUtils/XML::<parameters>  <algorithm name="sgsim" />     <Simulation_seed type="clock"/>  <Path type="random"><Seed type="clock"/></Path>  <Nb_processors  value="-2"  />    <Grid_Name value="gridxy0" />     <Property_Name  value="simtest0" reuse_property="0" />     <Nb_Realizations  value="3" />     <Max_Conditioning_Data  value="12" />     <Max_Conditioning_Simul_Data  value="12" />     <Search_Ellipsoid  value="'+searchelips+' '+searchelips+' 0  0 0 0" />    <Assign_Hard_Data  value="0"  />     <Hard_Data  grid="pointset0"   property="hardtest0"  />    <Covariance_input  structures_count="1" >    <Structure_1 type="Covariance">  <Two_point_model  contribution="1"  type="Spherical Covariance"   >      <ranges range1="'+varrange+'"  range2="'+varrange+'"  range3="0"   />      <angles azimuth="0"  dip="0"  rake="0"   />    </Two_point_model>    </Structure_1>  </Covariance_input>  </parameters>   ') 
real_319 = [] 
for i in range(int(3)): 
    real_319.append(sgems.get_property("gridxy0","simtest0__real%d" % (i))) 
fileout = "C://Users/Katherine/Documents/GitHub/SeniorDesign/current/current/5-2_out0.txt" 
with open(fileout,'w') as f: 
    for i in range(len(real_319[0])): 
        for j in range(len(real_319)): 
            f.write(str(real_319[j][i])) 
            f.write(' ') 
        f.write(' \n') 
f.close() 
