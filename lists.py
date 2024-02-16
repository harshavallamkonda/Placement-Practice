x = ["harsha","phani","navya","navya"]
print(len(x))
print(x[3])
print(type(x))
print(x[-1])

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Range of indexes

print(x[1:5])
if "navya" in x:
    print("Yep Present",x)
    
x[1] = "rockstar" 
print(x)
x.insert(6,"yoyo")
print(x)

#append
x.append("mawabro")
print(x)

#extending the existing list
y = ["amma","nanna"]
z = ("omg","crazy")
print(x.extend(z))
x.extend(y)
print(x)
x.remove("harsha")
print(x)
#POP Method

y.pop(1)
print(z)
x.clear()
print(x)

print(y[-1])

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

fruits =  ["sapota","jamakaya","applepandu"]
for b in range(len(fruits)):
    print(fruits[b])
    
ninja = ["1000r","H2"]
z = 0
while z < len(ninja):
    print(ninja[z])
    z = z+1

fruits = ["madikaaya","cheenipandu","pandakaya"]
kothalist = []
for j in fruits:
    if "i""j" in  j:
        kothalist.append(j)
print(kothalist)

#Sort Functionality
fruits = ["madikaaya","cheenipandu","pansakaya"]
fruits.sort()
fruits.sort(reverse=True)
print(fruits)
#So Basically reverse=True is nothing but when we want to make a list reverse we need to use this keyword

def myfunc(n):
    return abs(n - 50)
