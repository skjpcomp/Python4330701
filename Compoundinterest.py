p=int(input('enter principle amount'))
n=int(input('enter no of year'))
r=int(input('enter rate of interest'))
SI=p*r*n/100
print('simple interest=',SI)
t=int(input('enter no of year elapsed'))
CI=p*pow(1+(r/100*n),(n*t))
print('compound interest',CI)
