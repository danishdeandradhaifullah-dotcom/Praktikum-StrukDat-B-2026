mylist = ['Demoralize', 'Ego', 'Hinata']
print(mylist)
print("The list length is", len(mylist)) # how to check the length of the list
print(type(mylist)) # to find out what type it is

list1 = ["I'd", "never", "understand", 'man', 'man'] # it can carry strings
list2 = [1, 5, 7, 9, 3] # integers
list3 = [True, False, False] # and booleans
print(list1)
print(list2)
print(list3)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#check if items exists
thisList = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 