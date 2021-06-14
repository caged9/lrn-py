import sys

#recursive

def show_size_1(x, sum, level=0):
    # print(sys.getsizeof(x))
    if hasattr(x, "__iter__"):
        if hasattr(x, "items"):
            for xx in x.items():
                if not xx[0].startswith("__") and not hasattr(xx[1], "__call__") and not xx[0] == "sys":
                    # print(xx)
                    sum = show_size_1(xx, sum, level+1)
        elif not isinstance(x, str):
            for xx in x:
                sum = show_size_1(xx, sum, level+1)
    return sum + sys.getsizeof(x)
    
#non-recursive

def show_size_2(loc):
    size = 0
    for obj in loc.values():
        print(obj)
        print(sys.getsizeof(obj))
        size += sys.getsizeof(obj)
    print('#'*50)
    print('Memory used:',size)   

def sum_all_1(*args):
    res = 0
    for var in args:
        # print(var)
        res += show_size_1(var, res)
        # print(res)
    return res
        
def sum_all_2(loc):
    res = 0
    return show_size_1(loc, res)