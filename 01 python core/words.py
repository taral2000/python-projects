print("Hello World!")
list = ["test","Oranges","Apple"]
for i in list:
    print(i)

def modify(k):
    k.append("King")
    print("k = ", k) 

modify(list)
print("list = ", list)


#list list = [1,2,3], slicing
#del list[index]
#list.remove("itemname")
#list.insert(index,item)
#list.extend(anotherlist)
#list.reverse()
#list.sort(), list.sort(reverse=True), list.sort(key=callbleFunction)
#Dictionary dict(list(tuple)) dict = {"a": 1234, "b":12344}
#set data type
#   set = {6, 34, 3454, 23233} => duplicates are discarded, 
#   unordered list, muttable, used for set algebra
#Tuple t = (1,'test', 3.23)
#range range(stop), range(start, stop), range(start, stop, step)