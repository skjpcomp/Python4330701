print("enter date in format DD/MM/YYYY :")
date=input("enter date:")
date= date.split("/")
print("Date in format MM--DD-YYYY:%s-%s-%s"%(date[1],date[0],date[2]))