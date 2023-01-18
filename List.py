student=[15,'dhara','F',65,70]
print(student)
#Add Item in a list
student.append(80)
print(student)
student.insert(3,85)
print(student)
#Remove item from a list
student.remove(85)
print(student)
del student[2]
print(student)
student.pop()
print(student)

print('Number of elements in list',len(student))
#Access elements of the list using the index. 
print(student[0])
print(student[1])
print(student[2])
#Sort the list. 
list1=[3,8,1,2,6]
print('unsorted list',list1)
list1.sort()
print('sorted list',list1)
list1.sort(reverse=True)
print('list in descending order',list1)
#Reverse the list.
list2=[3,4,56,21,23]
print('original list is',list2)
list2.reverse()
print('Reverse List is',list2)