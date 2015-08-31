import profile
import time
import numpy as np

f = open("F:\Personal\MS project\Bouyancy calculator\part1_0.amf", "r").read()
start = time.clock()
count = 0
index_start = 1
index_end = 1
x_values = []
y_values = []
z_values = []
v1 = []
v2 = []
v3 = []      
triangles = []
Pretetrahedrons = []
index1 = 0
index2 = 0
TotalVolume = 0.000000000000000000
M = [[],[],[],[]]
tetrahedrons = []

def tetraVolume(x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4,tetra0,tetra1,tetra2,tetra3):
     global tetrahedrons
     global TotalVolume
     M = [[x1,x2,x3,x4],[y1,y2,y3,y4],[z1,z2,z3,z4],[1,1,1,1]]      
     if np.linalg.det(M) != 0 and ((tetra0 not in tetrahedrons) or \
       (tetra1 not in tetrahedrons) or (tetra2 not in tetrahedrons) or\
        (tetra3 not in tetrahedrons)):
         tetrahedrons.append(tetra0)
         tetrahedrons.append(tetra1)
         tetrahedrons.append(tetra2)
         tetrahedrons.append(tetra3)
         tetrahedrons.append('tetra')         
         TotalVolume = abs(0.16666666666666666*np.linalg.det(M)) + TotalVolume    

def find_string(str_start,str_end,array,option):  
    global index_start 
    global index_end 
    global count
    count = 0     
    index_start = 1
    index_end = 1
    limit = f.count(str_start)
    for i in range(0,limit): 
         index_start = f.find(str_start,index_start)
         index_end = f.find(str_end,index_end)
         if index_start != 0:
             #print f[index_start+ len(str_start):index_end]
             array.append(f[index_start+len(str_start):index_end])
             index_start = index_end
             index_end = index_end + 10
             count = count + 1
    print 'Number of instances of',str_start  ,' = ', limit
    if option == 1:
       return limit

def form_triangles():
    global v1
    global triangles
    global index1
    global index2
    index2 =0 
    global M
    global TotalVolume
    TotalVolume = 0
    global x_values
    global y_values    
    global z_values    
    
    for i in range(0,len(v1)):       
        triangles.append(v1[i])
        triangles.append(v2[i])
        triangles.append(v3[i])  
   
    v1 = map(int,v1)
    x_values = map(float,x_values)   
    y_values = map(float,y_values)
    z_values = map(float,z_values)
    triangles = map(int, triangles)
    index1_backup = 0
    for i in range(0,max(triangles)+1):
     index2 = 0 
     Pretetrahedrons[0:3] = [0]*4
     print i ,' of ',max(triangles)+1
     
     for j in range(0, len(triangles)):    
      try:
        index1 = triangles.index(i,index2)
        offset = index1%3       
        if offset == 0:
            if j == 0:
              Pretetrahedrons[0] =(triangles[index1])
              Pretetrahedrons[1]=(triangles[index1+1])
              Pretetrahedrons[2]=(triangles[index1+2])
              #index1_backup = index1
            else:
              if triangles[index1+1] in Pretetrahedrons:
                Pretetrahedrons[3] = (triangles[index1+2])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0     
              else:
                Pretetrahedrons[3] = (triangles[index1+1])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0 
            index2 = index2 + 3
        elif offset == 1:
            if j == 0:
              Pretetrahedrons[0]=(triangles[index1])
              Pretetrahedrons[1]=(triangles[index1-1])
              Pretetrahedrons[2]=(triangles[index1+1])
              #index1_backup = index1
            else:
              if triangles[index1+1] in Pretetrahedrons:
                Pretetrahedrons[3] = (triangles[index1-1])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0 
              else:
                Pretetrahedrons[3]  = (triangles[index1+1])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0 
            index2 = index2+3
        elif offset == 2:
            if j == 0:
              Pretetrahedrons[0]=(triangles[index1])
              Pretetrahedrons[1]=(triangles[index1-1])
              Pretetrahedrons[2]=(triangles[index1-2])
              #index1_backup = index1
            else:
              if triangles[index1-1] in Pretetrahedrons:
                Pretetrahedrons[3] = (triangles[index1-2])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0 
              else:
                Pretetrahedrons[3] = (triangles[index1-1])
                tetraVolume(x_values[Pretetrahedrons[0]],x_values[Pretetrahedrons[1]],\
                     x_values[Pretetrahedrons[2]],x_values[Pretetrahedrons[3]],\
                     y_values[Pretetrahedrons[0]],y_values[Pretetrahedrons[1]],\
                     y_values[Pretetrahedrons[2]],y_values[Pretetrahedrons[3]],\
                     z_values[Pretetrahedrons[0]],z_values[Pretetrahedrons[1]],\
                     z_values[Pretetrahedrons[2]],z_values[Pretetrahedrons[3]],\
                     Pretetrahedrons[0],Pretetrahedrons[1],Pretetrahedrons[2],\
                     Pretetrahedrons[3])
                Pretetrahedrons[3] = 0 
            index2 = index2 + 3
      except ValueError:
          continue     
                                                                                                                            
def main(): 
    global count
    count = 0
        
if __name__ == '__main__':
    main()
    countX = find_string('<x>','</x>',x_values,1)
    countY = find_string('<y>','</y>',y_values,1)
    countZ = find_string('<z>','</z>',z_values,1)
    countV1 = find_string('<v1>','</v1>',v1,1)
    countV2 = find_string('<v2>','</v2>',v2,1)
    countV3 = find_string('<v3>','</v3>',v3,1)
    form_triangles()
    finish = time.clock()
    #print triangles
    print ' Total time taken =  ', (finish - start) 
    print ' Total number of Pretetrahedrons =  ', Pretetrahedrons.count('<tetra>')
    #Volume of tetrahedron, quardinates as columns in matrix and last row filled with 1s
    print 'Total Volume = ', (TotalVolume*10**9)     

    
        
