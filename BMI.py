weight=int(input('Enter Weight'))
height=float(input('Enter Height'))
BMI=weight/(height*height)
print('BMI=',BMI) 
if BMI>=19 and BMI<=25:
 print('Healthy')
elif BMI>25:
 print('overweight')
else:
 print('underweight')