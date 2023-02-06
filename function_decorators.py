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
