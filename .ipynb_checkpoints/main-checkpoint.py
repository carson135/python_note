# from dog import MyClass

# # Create an instance of MyClass
# my_instance = MyClass()

# # Set some instance variables using the dictionary
# my_instance.set_attribute('name', 'Alice')
# my_instance.set_attribute('age', 30)
# my_instance.set_attribute('job', 'Engineer')

# # Access the instance variables
# print(my_instance.get_attribute('name'))  # Output: Alice
# print(my_instance.get_attribute('age'))   # Output: 30
# print(my_instance.get_attribute('job'))   # Output: Engineer

# # Remove an instance variable
# my_instance.remove_attribute('age')

# # Try to access the removed variable
# print(my_instance.get_attribute('age'))   # Output: None

# # Print the current state of instance variables
# print(my_instance)  # Output: {'name': 'Alice', 'job': 'Engineer'}

# import logging

# my_dict = {'name': 'zh', 'age': 8}
# logging.info("Dictionary contents: %s", str(my_dict))

from pathlib import Path
import datetime

path = Path('pi100m.txt')
pi_string = path.read_text()
my_birthday = '090703'
birthday = datetime.date(2000 + int(my_birthday[:2]), int(my_birthday[2:4]), int(my_birthday[4:]))
#print(pi_string[:7])
if my_birthday in pi_string:
    i = pi_string.index(my_birthday)
    # print(pi_string[:i+6])
    print(f'my birthday is: {birthday}')
    print(f'my birthday is begin at NO: {i} digits in PI')
    print(f'Total digits length of the current PI is: {len(pi_string)}')
    
s = "Hello, World!"
new_s = s[:-1] if s else s
print(new_s)  # 输出: "Hello, World"

