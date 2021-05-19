import sys

def show_size(loc):
    size = 0
    for obj in loc.values():
        #print(obj)
        size += sys.getsizeof(obj)
    print('#'*50)
    print('Memory used:',size)   