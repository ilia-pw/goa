# You Can't Code Under Pressure #1
def double_integer(i):
    return i * 2




# ver gavige


# Beginner - Reduce but Grow
def grow(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum

# Calculate average
def find_average(numbers):
    if len(numbers) == 0:
        return 0  
    return sum(numbers) / len(numbers)


# Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


# Double Char
def double_char(s):
    st = ""
    for i in s:
        st += i * 2
    return st

# ver gavige




# Sum of Cubes
def sum_cubes(n): 
        return sum(i**3 for i in range(1, n+1))






# 1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია


# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ


# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd





# number = ["ilia","vano","giorgi","saba","vaxo"]
# number.pop(2)
# number.insert(0,"giorgi")
# print(number)




num = ["ilia","vano","giorgi","saba","vaxo"]
len(num)
if len(num) // 2 == 0:
    print("List length is even")
else:
    print("List length is odd")






