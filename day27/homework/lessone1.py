# 1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ჯამი.
def num(num1, num2):

    print(num1 + num2) 


num(5,5)



# 2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.
def even_odd(number):
    if number % 2 ==0:
        print("even")
    else:
        print("odd")
    
even_odd(5)


# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი.
def positive_negative(num):
    if num == 5:
        print("positive")
    else:
        print("negative")

positive_negative(-5)



# 4)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.
def name(num):
    print("hello"+num)
name("ilia")

def name(num):
    print("hello"+num)
name("vano")

# 5)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.


def str(str1, str2):

    print(str1 + str2)
    
str("Hello", "world")



    






