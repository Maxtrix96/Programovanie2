def my_func():
    if "test" not in dir(my_func):
        test = "a"
        my_func.test = "a"
    
    print(my_func.test)
    print("done")
    

my_func()
my_func()

def my_func(example:list = []):
    print(example)
    example.append("chungus")
    

my_func()
my_func()