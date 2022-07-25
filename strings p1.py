# print("hello world")
a="hello world"
print(a.upper())                        # HELLO WORLD

print(dir(str))                      # we know string methods

print('hello python'.upper())           # HELLO PYTHON

a="HELLO WORLD"
print(a.lower())                           # hello world

print("HELLO world".lower())                #hello world
 
print("HELLO World".casefold())           # hello world

print('hELlo python'.isupper())             # False
print("HELLO WORLD".isupper())                   #TRUE

print("HELLO WOrld".islower())              # false 
print("hello world".islower())                 # True

print("hai bye".capitalize())                 # Hai bye

print("hello world".title())                   # Hello World

print('Hello world'.istitle())                 # False
print('Hello World'.istitle())                 # True    

print('pytHon CoDe'.swapcase())                  # PYThON cOdE

print('computer'.isidentifier())                  # True
print(' computer'.isidentifier())                 # False
print('5computer'.isidentifier())                  # False
print('_computer'.isidentifier())                  # False 

print(''.isspace())                                     # False
print('m'.isspace())                                    # False
print('     '.isspace())                                # True
print(' 1'.isspace())                                   # False  

