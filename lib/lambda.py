# create single-line, anonymous functions using the lamba keyword
new_dozen = lambda n : n + 12
new_dozen(3)
#  15

# function thst adds specific number when invoked
def my_func(x):
    return lambda n : n + x

def your_func(x):
    return lambda a, b: (a + b) * x

sum_times_2 = your_func(2)
sum_times_2(10, 20)
#  => 60

