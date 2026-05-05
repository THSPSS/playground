import random
#how about put random numbers in list that would be more fun
a = [random.randint(1,45) for _ in range(11)]
print(a)
#for loop to check all the element in list
#check if element is less than 5
print([num for num in a if num < 5])

