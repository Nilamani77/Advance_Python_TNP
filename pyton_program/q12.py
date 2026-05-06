global_var = 10

def modify_global():
    global global_var
    global_var = 20

modify_global()
print(global_var)