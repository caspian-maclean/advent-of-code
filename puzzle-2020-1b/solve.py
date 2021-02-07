
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
    for j in numbers:
        for k in numbers:
            if i+j+k == 2020:
                print(str(i)+"*"+str(j)+"*"+str(k)+"="+str(i*j*k))
 
#prints answer multiple times
#answer is: 907*1024*89=82660352 
