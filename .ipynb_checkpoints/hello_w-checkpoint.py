#import this
print("hello ni hao")
ms="\ta BC \n"
l = ms.lower()
cb = ms + l
print(cb)
#print(1.0+2.0)
addresses = ['bj', 'longgang', 200198, 4.0]
addresses.append(57)
# addresses.insert(4, 'abc')
print(addresses)
# #del addresses[1]
# addresses.remove(4.0)
# print(addresses)
# print(addresses[-3])
# addresses.reverse()
# print(addresses)
for i in addresses:
    if(i != "longgang"):
        print(i)
    
# r = range(1,7)
# rr = list(r)
# print(r)
# print(r[2])
# print(rr)
alien0 = {'color':'green', 'points':8, 99:100}
# print(alien0['color'])
# print(alien0['points'])
alien0['color'] = 'red'
alien0['x'] = 90
alien0['y'] = 80

#del alien0['points']
print(alien0.get('yy', 'no the key'))
print(alien0.get('gg'))

for k, vv in alien0.items():
    print(f"{k}: {vv}")
    
# if 'xx' in alien0.keys():
#     print('x is in the keys')
    
# print(sorted(alien0.keys()))
ss = set(alien0.values())
print(ss)
print(alien0[99])

ab = set(addresses)
print(ab)

#import make_pizza as pizza
from make_pizza import greet_test

#greet_user(addresses[1])
#print(pizza.greet_user('zhangg', loc='princeton', field='physics'))

print(greet_test('zhou', "34", "tianj", 5.8))

from dog import Dog

my_dog = Dog('jer', 8)
my_dog.name = 'jerrupdate'
my_dog.sit()

from pathlib import Path

path = Path('pi.txt')
contents = path.read_text()
print(contents)

writepath = Path('save.txt')
cont = 'abc is good place to visit ...\nenough, please go ahead.'
writepath.write_text(cont)



# import json
# path = Path('numbers2.json')
# if path.exists():
#     contents2 = path.read_text()
#     numbers= json.loads(contents2)
#     print(f"get {numbers} from json file")
# else:
#     t1 =  input('please input json contents')
#     path.write_text(json.dumps(t1))
#     print("i'll remember your input, ans save json file, and get by next time")

# while True:
#     sn = input('first number:')
#     if sn == 'q':
#         break
#     try:
#         answer = 9 / int(sn)
#     except ZeroDivisionError:
#         pass
#         #print('please input a non zero number')
#     else:
#         print(answer)

# c = input('please input:')
# print(int(c))

# inc = 0
# while inc < int(c):
#     print(inc)
#     inc +=1

# for t in addresses:
#     if t == 'bj':
#         addresses[1] = 55
#     # addresses.append(67)
        
# print(addresses)