""" favorite_language=' python'
print(favorite_language)
print(len(favorite_language))
ab = favorite_language.lstrip()
print(ab)
print(len(ab))
print(len(favorite_language))
print(favorite_language)

 
message='https://baidu.com/manager/sub21'
print(message)
print(message.removeprefix('https://'))
print(message.removesuffix('sub21'))


#print(len(favorite_language.rstrip()))


print(2+3-1)
print(2.3*2)
prin
bicycles=['names','things','wrongs',5]
print(bicycles)
print(bicycles[1].title())
print(bicycles[-1])
print(f'My first {bicycles[1].title()}')


bicycles=['names','things','wrongs',5]
print(bicycles)
bicycles.append(1)
print(bicycles)
bicycles.insert(0,5)
print(bicycles)

print(len(bicycles))

del bicycles[3]
print(bicycles)
print(bicycles.pop(1))
print(bicycles)

bicycles=['names','wrongs','things']
print(bicycles)
#print(bicycles)
#print(bicycles.remove(5)) 'a'
#print(bicycles)
#bicycles.sort()
#print(bicycles.sort())
#print(bicycles)
#print('i love computing programming with the greatest willing'.title())
bicycles.reverse()
print(bicycles)
bicycles.reverse()
print(bicycles)
print(len(bicycles))


persons=['cheng nanwei','zhang zhiyu','cheng ruyi']
for person in persons:
    print(f"{person.title()},that's good\n")
print("Thank you")

print(range(4,11))
print(type(range(3)))

for a in range(1,10):
    print(a)
    
b=list(range(1,1))
print(type(b))

a = '56'
print(type(a))
print(type(int(a)))  #interge

f = 579.234
print(f)
print(int(f))

print(type(str(f) ))

#b = 'nanwei'
for c in ["first", "second", "third"] :
    print (c)


i=list(range(2,11,3))
print(i)
a=[]
for b in range(1,10):
    c=b**2
    a.append(c)
print(a)
print(min(i))


a=[b for b in range(0,11)]
#print(a)
#a = ' abc defg'
#print(a[-1:])
#print(a)
b=a[:]
del b[1]
print(b)
print(a



a=[1,2,3,4,5,6,7,8,9,10]
a='b'
print(type(a=='b'))  #None bool True/False, int float str ' " list[] tuple ()
b='c'
#print(a==b)

d = bool(1)

f = False

if a == b :
    print('you are true')
    print('yes, i do')
    
print( [lists**2 for lists in [1,2,4]])

print( (a !=b and (2<=3) ) and ( False) )  # and or not

if (not False):
    print('yes yes')


#In Python, the in keyword is used to check for membership within various data structures or to iterate over them

#a = ['ab', 'cd', 'ef', 'nw']
#a = 'chen nwei'
a = ('god', 'like', 'string', 'plane', 'nw')
print('nw' in a)

import random

# 生成一个在1到10之间的随机整数（包含1和10）
random_integer = random.randint(0, len(a)-1)

print(f'a[{random_integer}] = {a[random_integer]}' )
#print(a[random_integer])
print(f'{a[random_integer]} to {print("good enough")}') # formatted string literals: can call method, expression, formate number, multiline, escape curly brace within f-strings, 
print(type(None))

name = "Alice"
age = 30
multiline_greeting = f
Hello, my name is {name}.
I am {{{age}}} years old.

print(multiline_greeting)
# Output:
# Hello, my name is Alice.
# I am 30 years old.

a=(1,2,3,4,5)
for b in a:
    print(b)
print(a=b)


a = "welcome to"
b = "my home"
c = a + ' ' + b
d = f'{a} {b}'
#print(c)
#print(d)
#e = a[-2:]

#a = [range(1,10)]
#for e in a:
    #print(e)
    
a = list(range(0,10))
print(a)
b = [c**2 for c in a]
print(b)
b.append(10**2)
print(b)
i = 0
for c in b:
    if c == 9:
        #b.insert(i, 7)
        del b[i]        
    i = i + 1

print(b)



#print(type(range(2)))
#print(sum(range(3,5)))
#if 5 in range(10): print('yes')
#print(3,5,7,"god",'aa')

a = {"first":"zhang", "last":"yu", 3:6, 4:"key is int",}
print(a)

for k,v in a.items():
    print(k)

print(type(a.values()))
a = []
for b in range(1,6):
    a.append(b)
print(a)

a[2] = a[2] + 5
print(a[2])

for c in range(0,len(a)):
    a[c] = a[c] + 2
print(a)

#imm

d = True
e = False
i = 0
for f in a:
    if f > 10 or f < 10:
        a[i] = a[i] + 10
    #else:
    i = i + 1
print(a)

print("你好中国")
while True:
    a = input("please input your name: ")
    if a == 'quit':
        break
    else:
        print(a)
        
print('end')
"""

""" a = {'color':'green','points':5}
#print(a['color'])
#a['color'] = 'blouse' + a['colort']
#print(a)
#b = a.get('color','no')
#print(b)
d = a['color']
for key, dd in a.items(): # dic_item class
    #print(f'\nKeyaaa: {key} | valueaaa= {value}')
    #if '' == type(d)
    print("\nkeyss:" + key + '  valueaa:' + str(dd))
    #print(f'Key: {key} | value: {dd}') """

""" aa = 'i love you'  
i = 45 
e1 = f'56 {}'
print(e1)
e2 = '56' + aa
print(e2) """
""" c = ['speed','color','points']
for message in a.keys():
    if message in c:
        print(f"The alien's {message} is good." )
        
print(a.keys())
 """

""" list_test = ['abc', 'efg', 'bc','bc']
list_test.sort()
print(list_test) 

ss = sorted(set(list_test))
print(ss)

for a in set (list_test):
    print(a)
    
sss = {2, 4, 5, 5}
print(sss) """

""" a = {'aaa':'bbb','ccc':'ddd'}

c = {'aaa':'eee','ccc':'dd'}

aa = [a, b, c]
for nw in aa:
    print(nw)
    
print(aa)



 """

""" a = []
for b in range(15):
    c = {'name':'nw','age': b}
    a.append(c)
for aa in a[:5]:
    print(aa)
print('...') """

# a = {'product_name': {'name':'table','color':'blue','size':'biggest'} ,'price':[20, 30, 50]}

# for bb in a['product_name'].values():
#     print(bb)
    
# for b in a['price']:
#     print(f'{a["product_name"]}: {b}')


# food = {'name':"tomato", 'size':'medium',  'price':[20, 30, 50]}

""" country = 'Paris'
flag1 = "I will go to "
flag2 = "to watch olympic games"
b = country.replace('Paris','Briton')
a = flag1 + b + ' ' + flag2 
print(f"{flag1}{b} {flag2}")
aa = '_'.join(a.split(' '))
c = aa[:20]
print(c)
for q in c:
    print(q)

d = a[-2]
#print(d)
#d = a[:1]
print(d)
 """

""" prices = list(range(33,99,6))
prices[0] = prices[0] + 2


print(prices)
for a in prices:
    i = prices.index(a)
    if not (a > 50 and a < 80):                
        prices[i] = prices[i] + 1
    print('the latest price is '+ str(prices[i]))  
print(prices) """

# tu = (2,3,4,2,5)

# print(tu[3])

# se = {2,3,5,2,3,6,7}
# for i in tu:
#     print(i)
    
# print(len(se))
# se.remove(3)
# #se.clear()
# print(se)

# Returns a new sorted list from the elements of any iterable.

# a = sorted('24oaedf1209', reverse=True)
# a = sorted({'test':'abc', 'are':'23d', '3':5}, reverse=True)
# a = range(10,1,-2)
# print(sorted(range(4), reverse=True))

# Returns a reversed iterator of the given sequence: 
# r1 = reversed('24oaedf1209')
# r2 = reversed({'test':'abc', 'are':'23d', '3':5})
# r3 = reversed(range(4))
# # print(r2)
# # print(next(r3))

# # Returns an iterator object. It is used to convert an iterable to an iterator.
# i1 = 'ag45872dsw'.split()
# i2 = iter("good.ensab")
# print(next(iter(next(i2))))

# for i in iter("good.ensab"):
#     print(i)

# if 'a' in i2: print(True)
# if 'sa' in "adfiwsade": print(True)

# t1 = type('godes')
# print()
# print(t1.isdigit("34er5"))
# print((dir("afdie wes")))
# print("dase we".center(20) + 'a')
# print('class'.isidentifier())

# a = ["df"]
# b = ["df"]
# print(id(a))
# print(id(a) == id(b))

# print(ord('中'))
# print(chr(22269))

# print(type(format(345.5642, ".2f")))

# print(ascii('Hello, 世界!'))
# print(chr(0X754c))

# # help(print)  # Displays the documentation for the print function

# class MyClass:
#     """This is a sample class."""
#     def my_method(self):
#         """This is a sample method."""
#         pass

# # help(MyClass)  #

# code = """
# def greet(name):
#     print(f'Hello, {name}')

# greet('Alice')
# """
# exec(code)  # Output: Hello, Alice

# help(time)

# s = "do you know how to fix the bug? if do, please tell me"
# a = s.replace('do', 'does')
# print(a)
# b = a.replace(' ','_')
# print(b)
# t = b.split('_')
# c = ' '.join(t)
# print(c)
# g = t.index('if')
# f = (t[:g])
# f.append('Ok')
# print(f)
# f.insert(-1,'please')
# print(f)
# f.remove('fix')
# print(f)
# n = f.index('please')
# f.pop(n)
# print(f)
# j = {'name':'nw'}
# j['dada'] = f
# print(j)
# print(len(j['dada']))
# i = 0
# for u in j['dada']:
#     i = i + 1
# print(i)
# l = 'dada number is '
# o = f'{l}{i}'
# print(o)

# p = l + str(i)
# print(p)

""" a = input('I well have a/an (toy):')
print(len(a)) """

# d = str()
# birth = []

# while d != 'n':
        
#     a = input('please input the person year of birthday:')
#     b = input('please input the person month of birthday:')
#     c = input('please input the person day of birthday:')
        
#     d = f'you input birthday is : {a}/{b}/{c}'
#     print(d)
#     birth.append(a + '/'+ b +'/' + c)
#     #print(birth) 
#     d = input('Do you want to input another person birthday.(yes = y / no = n)')
    
#     while d != 'y' and d != 'n':
#         d = input('Do you want to input another person birthday.(yes = y / no = n)')
    
#     if d == 'n': 
#         break
#     elif d == 'y':        
#         continue
    
# for f in birth:
#     print(f) 
        
# print('Good Bye!')
# sandwich_orders = ['a','b','c','pastrami','pastrami','pastrami']
# finished_sandwiches = []
# for y in sandwich_orders:
#     finished_sandwiches.append(y)
#     print('I made your ' + y)    
# print(finished_sandwiches)

# while 'pastrami' in sandwich_orders:
#     a = sandwich_orders.remove('pastrami')    
#     print(a)
# print(finished_sandwiches)
# print(sandwich_orders)
#g = True
# q = 'q'
# while True:
#     a = input('If you can go back your age, which years old you want to go?')
#     if a == q:
#         print('the game is over')
#         break
    
    
#     t = int(a)
#     print(f'i want go to {t} years old')

# a = input('How much people in the room')
# if int(a) > 8:
#     print('Sorry,have\'t enough seats')
# else:
#     print('Please come in')

# a = input('Please tell me a number:' )
# if int(a) % 10 == 0:
#     print('The number is multiple of 10')
 
""" while True:
    b = input('how old are you?')
    if b == 'q':
        break
    c = int(b)
    print(type(b))
    if c < 3:
        print('you are free.')
    elif c >= 3 and c < 12:
        print('please give me 10 dollars.')
    elif c >= 12:
        print('please give me 15 dollars.') """
    
# def a(b,c):
#     print('Hello!',b,'Hello!',c)
# a('cat','dog')
# for g in '程文威':
#     print(g, end= str())

# a = list(range(1,30))
# i = 0
# for t in a :
#     if a[i] % 3 == 0:
#         i == i + 1
#         print(a[i])
        
# k = list(range(1,11))
# c = [d**3 for d in k]
# print(c)
# for g in c:
#     print(g)

# a = list(range(1,10))
# for b in a:
#     if b == 1:
#         print('1st')
#     elif b == 2:
#         print('2ed')
#     elif b == 3:
#         print('3rd')
#     else:
#         print(str(b) + 'th')
# Active = True
# while Active: #b != 'quit':
#     b = input('How old are you?(input "quit" to quit the app)')
#     if b == 'quit':
#         Active = False
#     if b.isdecimal():
#         c = int(b)
#         if c < 3:
#             print('You are free.')
#         elif c >= 3 and c < 12:
#             print('Please give me 10 dollars.')
#         elif c >= 12:
#             print('Please give me 15 dollars.')

# def make_shirt(side,word = 'I love python.'):
#     print('The T-shirt is ' + side + " and here is " + word)
#     print(f"The T-shirt is {side} and here is {word}")
# #make_shirt('M','Hello')
# make_shirt('L')
# make_shirt('M')

# def describe_city(city,country = 'China'):
#     print(f'{city} is in {country}')
# describe_city('Beijing')
# describe_city('Shanghai')
# describe_city('Tokyo','Japan')

# def a(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# def length_of_string(str1):
#     print((str1))
#     i = 0
#     for c in str1:   
#         i += 1     
    
#     return i

# str2 = 'test users number?'
# print(f'the length of the string: {str2} is {length_of_string(str2)}')

# v = len(str2)

# ll = [2,7,5,3]

# # a = ll.pop()

# print(ll.sort())
# def return_string():
    # a = 'abc'    
    # return a

# return_string()
    # print(a.title())
    # print(a)
    # # print('abc'.title())

# def name(first_name,middle_name,last_name):
# #     print(first_name + ' ' + middle_name + ' ' + last_name)
# # name('a','b',)
#     full_name = f"{first_name} {middle_name} {last_name}"
#     full_name.title()
    
    
# a = name('a','b','c')
# print(a)

# Active = True
# while Active:
#     a = input('How old are you?')
#     if a == 'quit':
#         break
#     # print(a)
    
#     if a.isnumeric():
#         b = int(a)
#         #print(None)
#         if b < 3:
#             print('Free')
#         elif b >= 3 and b < 12:
#             print('10 dollars')
#         elif b >= 12:
#             print('15 dollars')
#     else:
#         print('Please input your years old.')

# def city_country(city,country):
#     a  = f'\n{city},{country}'
#     return a

# while True:
    
#     city = input("city name:")    
#     if city == "q":
#         break
    
#     country = input("country name:")
#     if country == "q":
#         break
    
#     b = city_country(city,country)
#     print(b)

# def make_album(singer,album, number = None):
#     a = {'singer': singer, 'album':album}
#     if number :
#         a['number'] = number
#     return a
    
# while True :    
    
#         singer = input('please input the album singer:')
#         if singer == 'q':
#             break
        
#         album = input('please input the album name:')
#         if album == 'q':
#             break
        
#         number = input('please input number of the album if you want, or input "enter" to ignore it:')
#         if number == 'q':
#             break
#         elif number == '':
#             a = make_album(singer,album)
#         else:
#             a = make_album(singer,album,number)
        
#         print(a)



# a = ['a', 'b', 'c']
# def show_messages(a):
#     for b in a :
#         print(b)
        
# # sent_messages = []
# # while a:
# #     sent_messages.append(a.pop())

# # sent_messages.reverse()
# # print(sent_messages)

# def sent_messages(messages_list):
#     i = 0
#     for b in messages_list:
#         i = messages_list.index(b)
#         messages_list[i] = b + '1'
#     print(messages_list)    

# sent_messages(a[:])
# print(a)

# from nwm import sandwich,make_car,add1

# a = sandwich('a','b','c')
# print(a)

# # a = make_car()

# c = add1('1','2')
# print(c)

# d = add1(1,2)
# print(d)

# e = [1,2,3]
# print(sum(e))



# list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flattened = [item for sublist in list_of_lists for item in sublist]
# print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# from nwm import sandwich

# sandwich("big", "pepper", "cheese", size="middle")

# import nwm
# nwm.sandwich('big','pepper', 'cheese')

# from nwm import sandwich
# sandwich('big','pepper', 'cheese')

# from nwm import sandwich as sand
# sand('big','pepper', 'cheese')

# import nwm as nw_m:
# nw_m.sandwich('big','pepper', 'cheese')

# from nwm import *
# sandwich('big','pepper', 'cheese')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        print(f"The restaurant name is {self.name}")
        print(f"{self.type} is my favorite")
        
    def describe_restaurant(self):
        print(f"The restaurant has long history")
        
    def open_restaurant(self):
        print(f"The restaurant is now open")
        
restaurant_name1 = Restaurant('ne', 'Sichuan cuisine')
restaurant_name2 = Restaurant('hr', 'Guangdong cuisine')

restaurant_name1.describe_restaurant()
restaurant_name2.describe_restaurant()

restaurant_name1.open_restaurant()
    





























