#LISTS
mylist = ['Demoralize', 'Ego', 'Hinata', 'Staple', 'Laufey', 'Dragon']
print(mylist) # printing the list you made
print("The list length is", len(mylist)) # how to check the length of the list
print(type(mylist)) # to find out what type it is
print(mylist[2:5]) # range of indexes the first one is where it starts the second one is where it ends not counting it
print(mylist[:3]) # by leaving out the start it just starts from the beginning


list1 = ["I'd", "never", "understand", 'man', 'man'] # it can carry strings
list2 = [1, 5, 7, 9, 3] # integers
list3 = [True, False, False] # and booleans
print(list1)
print(list2)
print(list3)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#check if items exists
if "Ego" in mylist: # you can use an if statement to check if an item is in the list
  print("Yes 'Ego' is in the list ")

#change items
newList = ["Sagittarius", "Cancer", "Libra", "Capricorn", "Aries", "Taurus"]
newList[2] = "Leo" # change the list by using index
newList[3:4] = ["Virgo", "Gemini"] # change a range 
newList.insert(4, "Scorpio") # insert an item by first putting where you want to insert it then add the element
print(newList)

#add items
newList.append("Aquarius") # using append you can add a new element, it automatically gets inserted at the end
print(newList)
newList.extend(mylist) # using extend we can mesh two lists together
print(newList)

#remove items
NewList = ["This", "World", "Concrete", "Flowers", "Grow"]
NewList.remove("This") # remove using .remove by typing in element
NewList.pop(1) # using pop removing with an index
NewList.pop() # if not specified it will just remove the last element
print(NewList)
NewList.clear() # clear to clear out the entire list
print(NewList)

#Loop
_list = ["Each", "Stage", "I'll", 'Move', 'Through']
for x in _list: # for loop
  print(x)

for i in range(len(_list)): # you can use range
  print(_list[i])

a = 0
while a < len(_list): # and also while
  print(_list[a])
  a = a + 1

#List comprehension
List = ["Hades", 'Zeus', 'Hera', 'Aphrodite', 'Artemis']
ListNew = []
ListThird = []

for b in List:
  if "s" in b: # if an element of the list contains an "s" it will append it to the new list  
    ListNew.append(b)

ListThird = [c for c in List if "s" in c]

NewerList = [b.upper() for b in List] # .upper to make stuff uppercase

print(ListNew)
print(NewerList)

#Sort lists
NewestList = ["You're", "Just", "Dead", "Man", "Mewtwo"]
NewestList.sort() # .sort to print items alphanumerically
NewestList.sort(reverse= True) # use reverse to reverse it
print(NewestList) 

#Copy list
oneList = List.copy() # copy a list onto another by using .copy
twoList = list(List) # you can also use the list method
print(oneList) 
print(twoList)

#join lists
OneList = ["I'm", "Just", "A", "Man"]
TwoList = ["Somebody", "That", "I", "Used", "Know"]

ThreeList = OneList + TwoList # combine two strings

for z in TwoList:
  OneList.append(z)
print(ThreeList)
print(OneList)