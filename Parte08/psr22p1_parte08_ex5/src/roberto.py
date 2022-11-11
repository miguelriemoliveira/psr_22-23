
global_var = 5
global_lst = [1,2,3]

def func1():
    global global_var # optional
    c = 4

    # read from global_var
    d = c + global_var

    print(global_lst)
    
    
def func2():    
    global global_var # optional
    a = 7
    b = 5

    global_var = a + b

    global_lst.append(4)

func1()
func2()
print(global_lst)