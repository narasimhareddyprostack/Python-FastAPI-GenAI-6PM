'''
filter(function,sequence) 
'''
numbers=[1,2,3,4,5,6,7,8,9,10]

def check_even(num):
    return num%2==0


filter_obj=filter(check_even,numbers)
#Exectuing check_even function every element of sequence ie numbers
print(filter_obj)
print(list(filter_obj))
