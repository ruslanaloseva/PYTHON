numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_ = numbers [0:4] + numbers [5:20]
sum_ = sum(numbers_)
len_ = len(numbers)
sr_ = sum_ / len_
numbers [4] = sr_
print( "Измененный список", numbers)


