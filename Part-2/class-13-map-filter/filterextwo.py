numbers=[1,2,3,4,5,6,7,8,9,10]

def check_even(num):
    return num%2==0

lambda num:num%2==0

#filter(lambda num:num%2==0,[1,2,3,4,5,6,7,8,9,10])
even_numbers=list(filter(lambda num:num%2==0,[1,2,3,4,5,6,7,8,9,10]))
print(even_numbers)