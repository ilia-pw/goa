
# Function 1 - hello world
def greet():
    return  "hello world!"


# Opposite number
def opposite(number):
    return -number
  
# Return Negative
def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number


# Sum of positive
def positive_sum(arr):
        sum = 0
        for i in arr:
            if i > 0:
                sum += i
        return sum




# String repeat
def repeat_str(repeat, string):
    return repeat * string


# ver gavige






# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)



# Remove String Spaces
def no_space(x):
    return x.replace(" ","")







# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)
            