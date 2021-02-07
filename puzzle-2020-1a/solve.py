
inputfile = open("input.txt")
lines=inputfile.readlines()

#length of list
n=len(lines)

#convert to array of numbers
numbers=[]
for i in range(n):
    numbers.append(int(lines[i]))

#test converted numbers
#print(numbers[0]+numbers[199])

for i in numbers:
    #print(i)
    for j in numbers:
        if i+j == 2020:
            print(str(i)+"*"+str(j)+"="+str(i*j))
 
#prints answer twice, once with the first number as i, once with the first number as j
#answer is: 1926*94, or 181044
