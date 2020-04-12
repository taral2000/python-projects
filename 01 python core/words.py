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
#Tuple t = (1,'test', 3.23)
#range range(stop), range(start, stop), range(start, stop, step)