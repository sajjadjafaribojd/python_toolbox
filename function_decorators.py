# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.
  
# Adds a welcome message to the string
def welcome_message(str):
    def add_welcome():
        return 'Welcome to '

    return add_welcome() + str    

def site(site_name):
    return site_name

print(site('JabJ.ir'))  #JabJ.ir
print(welcome_message(site('JabJ.ir'))) #Welcome to JabJ.ir  


#A decorator is a function that takes a function as its only parameter and returns a function.

# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().

def welcome_message_0(func):
    # Nested function
    def add_weblcome(site_name):
        return 'Welcome to ' + site_name

    # Decorator returns a function
    return add_weblcome    

@welcome_message_0
def site_0(site_name):
    return site_name

print(site_0('jabj.ir')) #Welcome to jabj.ir

# https://www.geeksforgeeks.org/chain-multiple-decorators-in-python/
# chain-multiple-decorators-in-python
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        print('Hello 2')
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        print('Hello 1')
        return 2 * x
    return inner
 
@decor1 #priority 2
@decor  #priority 1
def num():
    return 10
 
print(num()) # Hello 1 Hello 2 400


def decor1(func):
        def wrap():
               print("************")
               func()
               print("************")
        return wrap

def decor2(func):
        def wrap():
               print("@@@@@@@@@@@@")
               func()
               print("@@@@@@@@@@@@")
        return wrap

def decor3(func):
        def wrap():
               print("!!!!!!!!!!!!!")
               func()
               print("!!!!!!!!!!!!")
        return wrap        
     
@decor1
        
@decor2

@decor3
def sayhellogfg():
         print("Hello")

@decor1
        
@decor2

@decor3         
def saygfg():
         print("GeekforGeeks")
         
sayhellogfg()
saygfg()



# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
@decor
@decor1
def num2():
    return 10
   
print(num())
print(num2())