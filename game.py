maximumlength = 3
def grid_view(list):
    col_count = 0
    list2 =[]
    for i in range(0, maximumlength):
        list1 = []
        for j in range(0, maximumlength):
            if(col_count in list):
                list1.append(True)
            else:
                list1.append(False)
            col_count += 1
        list2.append(list1)

    return list2

def position_true(list):
    pos = []
    for i in range(0, maximumlength):
        for j in range(0, maximumlength):
            p = []
            if(list[i][j] == True):
                p.extend([i,j])
                pos.append(p)
    return pos