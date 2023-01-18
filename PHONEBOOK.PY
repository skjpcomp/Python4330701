#Creating a dicitonary name CONTACT with few contacts
contact={"diya":7863808488,"vidhi":7096019826,"nancy":7984584354,"mitanshu":9016067056,"suryaveer":8866368591}
'''def checkupper(name):
    for k in contact.keys():
        name==k.upper()
        number=contact.items()
        contact.update({name:number})
    print(contact)
checkupper('name')'''
'''def edit():
    choice=input('What do you want to change?\n a.Name\n b.Number\n')
    if choice==a:
        old=input('Enter previous name:')
        new=input('Replace with name:')'''
        
#Creating a function name add for adding new contacts in CONTACT    
def add(name,number):
    name=input("Enter name:")
    number=int(input("Enter number:"))
    contact.update({name:number})
    print('Contact saved!')

'''def search(find):
    print('Enter value correctly')
    find=input("Search:")
    if find in contact:
        print(name1,":",contact[name1])
    else:
        print("Not found!")'''
#Creating a function name DISPLAY  to display contacts          
def display():
    print('Name\t\tNumber')
    for key in contact:
        print("{}\t{}".format(key,contact.get(key)))
#Creating a function name DELETE to remove contacts from CONTACT 
def delete(name3):
    remove=input("Enter name to be removed from contact:")
    contact.pop(remove)
    print('Contact deleted')
#Here,it will display a menu for user to enter his/her choice
while 1:
    x="PHONE BOOK"
    y=x.center(20)
    print(y)
    print('\n 1.Add new contact\n 2.Search contact\n 3.Display contact\n 4.Delete contact\n 5.Exit\n')
    option = int(input("Enter your choice:"))
    if option==1:
        add('name','number')
    elif option==2:
        search('name1')
    elif option==3:
        display()
    elif option==4:
        delete('remove')
    elif option==5:
        break;
        
      