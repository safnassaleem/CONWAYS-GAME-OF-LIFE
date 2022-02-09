from collections import Counter
maximumlength = 4
def grid_view(l):
    col_count = 0
    list2 =[]
    for i in range(0, 4):
        list1 = []
        for j in range(0, 4):
            if(col_count in l):
                list1.append(True)
            else:
                list1.append(False)
            col_count += 1
        list2.append(list1)
    return list2

def position_true(l):
    pos = []
    for i in range(0, 4):
        for j in range(0, 4):
            position= []
            if(l[i][j] == True):
                position.extend([i,j])
                pos.append(position)
    return pos

def neighbours(list,i):
    true = []
    false = []
    if (i[1]-1 >= 0 and i[0]-1 >= 0):
        if( list[i[0]-1][i[1]-1] == True):
            true.append('y')
        elif (list[i[0]-1][i[1]-1] == False):
            pos=[]
            pos.extend([i[0]-1,i[1]-1])
            false.append(pos)
        
    if (i[0]-1 >= 0):
        if(list[i[0]-1][i[1]] == True):
            true.append('y')
        elif (list[i[0]-1][i[1]] == False):
            pos=[]
            pos.extend([i[0]-1, i[1]])
            false.append(pos)
                
    if (i[1]+1 < 4 and i[0]-1 >= 0):
        if( list[i[0]-1][i[1]+1] == True):
            true.append('y')
        elif (list[i[0]-1][i[1]+1] == False):
            pos=[]
            pos.extend([i[0]-1, i[1]+1])
            false.append(pos)

    if (i[1]-1 >= 0):
        if( list[i[0]][i[1]-1] == True):
            true.append('y')
        elif (list[i[0]][i[1]-1] == False):
            pos=[]
            pos.extend([i[0], i[1]-1])
            false.append(pos)
        
    if (i[1]+1 < 4):
        if(list[i[0]][i[1]+1] == True):
            true.append('y')
        elif (list[i[0]][i[1]+1] == False):
            p=[]
            p.extend([i[0], i[1]+1])
            false.append(p)
        
    if (i[1]-1 >= 0 and i[0]+1 < 4):
        if(list[i[0]+1][i[1]-1] == True):
            true.append('y')
        elif (list[i[0]+1][i[1]-1] == False):
            p=[]
            p.extend([i[0]+1, i[1]-1])
            false.append(p)

    if (i[0]+1 < 4):
        if(list[i[0]+1][i[1]] == True):
            true.append('y')
        elif (list[i[0]+1][i[1]] == False):
            p=[]
            p.extend([i[0]+1, i[1]])
            false.append(p)
               
    if (i[1]+1 < 4 and i[0]+1 < 4):
        if(list[i[0]+1][i[1]+1] == True):
            true.append('y')
        elif (list[i[0]+1][i[1]+1] == False):
            p=[]
            p.extend([i[0]+1, i[1]+1])
            false.append(p)
    
    return len(true), false


def change_status(list):
    new_list = list.copy()
    x = position_true(list)
    false_nb = []
    die = []
    for i in x:
        true_cells, false_cells = neighbours(list,i)
        if(true_cells < 2 or true_cells > 3):
            die.append(i)
        false_nb.extend(false_cells)
    for i in die:
        list[i[0]][i[1]] = False
    count = Counter([tuple(i) for i in false_nb])
    for key, value in count.items():
        if (value == 3):
           new_list[key[0]][key[1]]=True

    return new_list

