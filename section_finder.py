def half(x):
    if x[0] > 0:
        return 1
    elif x[0] == 0:
        return 0
    return -1

def quardrant(x):
    sec = half(x)
    if sec == 0 or x[1] == 0: return 0
    if sec == 1:
        if x[1] > 0:
            return 1
        else:
            return 4
    else:
        if x[1] > 0:
            return 2
        else:
            return 3
        
def octant(x):
    sec = quardrant(x)
    if sec == 0 or x[2] == 0: return 0
    if(x[2] > 0):
        return sec
    else:
        return sec+4

def sedecimant(x):
    sec = octant(x)
    if sec == 0 or x[3] == 0: return 0
    if(x[3] > 0):
        return sec
    else:
        return sec+8
    

def select_fn(dim:int):
    if dim == 1:
        return half
    elif dim == 2:
        return quardrant
    elif dim == 3:
        return octant
    elif dim > 3:
        return sedecimant
    else: raise ValueError("Invalid dimension")