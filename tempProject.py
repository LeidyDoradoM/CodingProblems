# Program that calculates the average high temperature of a given number of days
import numpy as np

n = int(input('How many day`s temperatures: '))
temps = np.zeros(n)

for i in range(0,n):
    temps[i] = int(input('Day '+str(i+1)+'`s high temp.: '))

#compute average
average = sum(temps)/n
print('Average: ', average)
#compute how many days are above average temp
count =0
for temp in temps:
    if temp-average > 0 :
        count = count+1
        
print(str(count)+' day(s) above average')
