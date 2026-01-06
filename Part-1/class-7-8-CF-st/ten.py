numbers=[11,7,8,12,1055,232,18,4]

#print n number of  even numbers from list
#print n number of odd numbers from list

even_count=0

for num in numbers:
    if num%2 == 0:
        even_count=even_count+1 


print("No of Even Numbers from list:", even_count)