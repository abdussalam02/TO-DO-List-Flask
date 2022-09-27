# This is *args 
# It alllows multiple parameters and stores it in tuple data type
def aladdin(*a):
    a = list(a)
    add = a+a
    print(type(add))
    
    return add

aladdin([1,2],[2,4])

# This is **kwargs
# It allows multiple parameters in key value form and stores it in a dictionary  
def salam(**kwargs):
    return kwargs, type(kwargs)

salam(a=10, b=20, c=40)