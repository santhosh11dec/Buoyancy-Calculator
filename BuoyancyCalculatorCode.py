import profile
import time
import numpy as np

f = open("F:\Personal\MS project\Bouyancy calculator\Body frame.txt", "r").read()
start = time.clock()
count = 0
index_start = 1
index_end = 1
x_values = []
y_values = []
z_values = []      
      
def find_string(str_start,str_end,array):  
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
    return limit
                            
def main(): 
    global count
    count = 0
        
if __name__ == '__main__':
    main()
    countX = find_string('<x>','</x>',x_values)
    countY = find_string('<y>','</y>',y_values)
    countZ = find_string('<z>','</z>',z_values)
    finish = time.clock()
    print ' Total time taken =  ', (finish - start) 
    
    #f.close()  
          

    
        
