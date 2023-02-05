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


