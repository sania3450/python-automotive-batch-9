myset={"apple","banana",
"grape","apple",False,0,2,True,1} 
mylist = ('a','b')
myset2={"a","n"}
#true = 1 boolean value
#false = 0 bool value
print(mylist)
empty_set = set()
empty_dict ={}
print(type(empty_set))
print(type(mylist))
#mylist.add(10)
myset.update(mylist)
count=len(myset)
print(myset|myset2) #union
print(myset&myset2) #intesection
for fruit in myset:
    print(fruit)

'banana' in myset #lh of in is a subset of rhs of in
