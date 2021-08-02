#Add function
def add(x,y):
    return x+y
#Subtract function
def subtract(x,y):
    return x-y #On master
#Multiply function
def multiply(x,y):
    return x*y  # on bug456
#Divide function
def divide(x,y):
    if y==0:
        return DIVIDE_BY_0-ERROR
    else:
        return x/y   #On Master
# Square Function
def square(x):
    pass