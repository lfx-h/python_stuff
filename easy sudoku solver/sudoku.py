import math
def sudoku(m):
    def missing(array): #missing numbers in a block
        complete = (1,2,3,4,5,6,7,8,9)
        return [i for i in complete if i not in array]

    def block(x):#function yields dict with key:location
        y=x
        for _ in range(x):
            if y<=3:
                break
            y-=3
        return [{m[i][j]:(i,j)} for i in range(3*math.ceil(x/3)-3,3*math.ceil(x/3)) for j in range(3*y-3,3*y)]

    def check_incomplete(array):
        return any(0 in row for row in array)

    while(check_incomplete(m)):
        for b in range(1,len(m)+1):
            for k,d in enumerate(block(b)):
                for key, location in d.items():
                    if key == 0:
                        missing_array = missing([key for d in block(b) for key,_ in d.items()])#missing values in block
                        for i,x in enumerate(missing_array):
                            if x in m[location[0]] or x in list(zip(*m))[location[1]]:
                                    pass
                            else:
                                try:
                                    for d2 in [item for e,item in enumerate(block(b)) if e!=k]:
                                        for key2, location2 in d2.items():
                                            if key2==0:
                                                if x in m[location2[0]] or x in list(zip(*m))[location2[1]]:
                                                    pass
                                                else:
                                                    raise #non unique number -> raise
                                    m[location[0]][location[1]]=x #apppends to location in original array
                                except:
                                    pass
    return m

'''
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
          '''
