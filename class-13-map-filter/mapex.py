numbers=[1,2,3,4,5,6,7,8]
def plusfive(num):
	return num+5

#map(function,seq)
map_obj=map(plusfive,numbers)
new_numbers=list(map_obj)
print(numbers)
print(new_numbers)