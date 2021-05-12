# map filter and reduce

# map function takes in a function and uses function to every element in the list
my_list = [2,6,8,3,1]
print(list(map(lambda x: x + 2, my_list)))

import statistics

data = [ 1,3, 7.5,5,3, 9,6,3,2]

avg = statistics.mean(data)

print(avg, list(filter(lambda x: x >avg, data)))





