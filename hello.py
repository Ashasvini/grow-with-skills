print("hello world") #prints hello world
'''to print a string'''
print(type("hello world")) #prints <class 'str'>
'''to check the type of the string'''
print(len("hello world")) #prints 10 
'''to check the length of the string'''
print("hello world".upper()) #prints HELLO WORLD
'''to convert the string to uppercase'''
print("hello world".lower()) #prints hello world
'''to convert the string to lowercase'''
print("hello world".capitalize()) #prints Hello world
'''to capitalize the first letter of the string'''
print("hello world".title()) #prints Hello World
'''to capitalize the first letter of each word in the string'''
print("hello world".replace("world", "viewers")) #prints hello viewers 
'''to replace a substring in the string'''
print("hello world".find("world")) #prints 6 
'''to find the index of a substring in the string'''
print("hello world".isalpha()) #prints False 
'''to check if the string contains only alphabetic characters'''
print("hello world".startswith("hello")) #prints True 
'''to check if the string starts with a substring'''
print("hello world".endswith("world")) #prints True 
'''to check if the string ends with a substring'''
print("hello world".split()) #prints ['hello', 'world'] 
'''to split the string into a list of words'''
print("hello world".count("l")) #prints 3
'''to count the number of occurrences of a substring'''