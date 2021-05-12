# prints all values in string format with space
x = [1,5,7]
print(*x) 

"""*args, **kwargs non keyword arguments and keyword arguments are used when it is not sure how many arguments are
will be needed for function """
def number_sum(*num):
    sum = 0

    for n in num:
        sum += n

    print(f"Sum = {sum}")

number_sum(3,7)
number_sum(1,7,9)

def data(**data):

    for key, value in data.items():
        print("{} is {}".format(key, value))
data(Firstname = "John", Lastname = "Mario", age = 55)
