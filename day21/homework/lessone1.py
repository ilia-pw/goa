# 1)კომენტარებით ახსენით განსხვევება indexing-სა და sliceing-ს შორის.
# ინდექსინგით გამოგვაქვს ერთი ელემენტი სიიდან/სტრინგიდან
# სლაისინგით რამოდენიმე ელემენტი გამოგვაქვს სიიდან/სტრინგიდან




# 2)შექმენით სია სადაც გექნებათ 5 ელემენტი და მინუს ინდექსების გამოყენებით გამოიტანეთ ბოლო 3 ელემენტი
numbers = [0,1,2,3,4]

print(numbers[-3:])



# 3)შექმენით სია სადაც გექნებათ 10 რიცხვი, გადაუარეთ ამ სიას და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია ან ტოლია 10ზე
num = [10,9,5,4,30,50,13,1,15,6]

for i in num:
    if i >= 10:
        print(i)



# 4)კომენტარის სახით ახსენით რა არის ფუქნცია, რაში ვიყენებთ და ჩამოწერეთ ყველა ნასწავლი ფუნქცია (გვერდით მიუწერეთ მათი დანიშნულება)
print()
input()
float()
range()
type()
int()
str()

# 5)(***BOSS LEVEL***) მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ უნდა თუ არა რომ მისი გვარი გადაიყვანოს დიდ ასოებად, თუ 
# გიპასუხათ "yes" მაშინ დაუბეჭდეთ
# მისი სახელი დიდი ასოებით, თუ გიპასუხათ "no" დაუბეჭდეთ უბრალოდ მისი სახელი. (მინიშნება: გაკვეთილის ბოლოს განვიხილეთ ზედაპირულად)

surname = input("შეიყვანეთ თქვენი გვარი: ")

question = input("გსურთ თუ არა თქვენი გვარი დიდად რომ დავწეროთ: ")

if question == "yes" :
    print(surname.upper())

elif question == "no" :
    print(surname)



