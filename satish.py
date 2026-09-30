"""
n=int(input("enter a number : " ))
if 0<n:
    print("positive")
elif 0>n:
    print("negative")
else:
    print("zero") 
    
age = int(input("enter your age : "))
if age >= 18:
    print("you are eligible to vote")
else:
   print("your are not eligible vote ") 

marks=int(input("enter your marks : "))
if 90<=marks<=100:
    print("A grade")
elif 75<=marks<=89:
    print("B grade")
elif 60<=marks<=74:
    print("C grade")
elif marks > 100:
    print("not consider")    
else:
    print("fail") 
# new program     
n = int(input("enter number"))
if 2 % n == 1:
    print("even")
else:
    print("odd")

n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))
n3 = int(input("enter third number : "))
    
if n1 > n2 and n1 > n3:
    print("first number is greater")
elif n1 == n2 == n3:
    print("both numbers are equal")
elif n2 > n3 and n2>n1:
    print("second number is greater")
else:
    print("third number is greater")
"""
"""    
n1=int(input("enter first number " ))
n2 = int(input("enter second number " ))
user = input()
if user == "+" :
    print(n1+n2)
elif user == "-" :
    print(n1-n2)
elif user == "*" :
    print(n1*n2)
elif user == "/" :
    print(n1/n2)
else:
    print("invalid operator")


my_list = ["apple" , "cherry" , "potato" ,"tomato" , "goa" , "banana"]
print(my_list)
k = input("enter your fruit:  ")
if k in my_list :
    print("yes")
else:
    print(k,"not in your list")
#item = my_list[]
my_list.append("lemon") 
print(my_list) 
f = my_list.pop() 
print(f)
print(my_list)
print(len(my_list))
my_list.insert(2,"grapes")
print(my_list)
#k1 . my_list()
#print(k1)
f = my_list.remove("apple")
print(my_list)
my_list.reverse()
"""
"""
list = [-5,-6,-3,-4,-2,-1,-8,-9,9,8,7,hi,6,5,5,4,4,3,3,2,2,1]
list.sort()
print(list)

"""
"""
#pattern try not understand the concept
for i in range(1,5):
    print(i)
    if i <= 5:
        print(i,end = " ")
        i = i+1
"""



""""
list = ["apple","berry","tomato","goa","pineapple","banana"]
print(list,end = " ")
new_list = list.sort()
print(list)
print(new_list)
""" 


"""
list1 = [0,9,8,7,6,5,4,3,2,1]
list2 = [5,6,4,3,2,9,10]
newlist = list1 + list2
print(list1)
print(list2)
print(newlist)
"""

"""
list = ["king","tomato = 69","banana","apple","cherry","goa"]
list1 = ["apple","cherry","goa"]
print(type(list1))
print("your list is here  : ", list)
k = ["hi",]
print(type(k))
print(list.pop(-1))
#print(list1(::-1)
print(list.pop(1))
"""


"""
#pattern printing practice
for i in range(1,5) :
    #print(i)
    print(i)
    #i = i + 1
    if i <= 5:
        
        print(i,end = " ")
        i = i + 1
        if i == i :
            print(i)
"""

"""
for i in range(1,5):
    #print(i,)
    i = i + 1
    if i<=5:
        print(i)
        i = i + 1


for i in range(10,0,-2):
    print(i,end = " ")
    

def add(a,b):
    result = a+b
    return result
a = int(input("enter a1 value : "))
b = int(input("enter b1 value : "))
  

answer = add(a,b)
print("addition = ",answer)
print("addition = ",answer)
print("addition = ",answer)
print("addition = ",answer)



# k = admin
# p = 1234

username = input("enter username : ")
password = input("enter password : ")
if "admin" == username and "1234" == password :
    print("username and password correct ")
    print("******* login successfull *********")
elif username == "admin " and password != "1234":
    print("wrong password")
else:
    print("wrong username")    

# elif username != "admin" and password == "1234" :
#     print("wrong username")

else :
    print(" both are not given correct credetials")





    # print( n = balance - amount ,"here it is remaining ba
    # lance")
    balance = balance - amount
    print("withdrawl succesful")
    print("Remaining balance : " , balance)


    if balance < 500 :
        print("minimum balance warning ")
amount = int(input("enter amount : "))
balance = int(input("enter balance"))
if amount <= 0 :
    print("invalid sufficient amount" , amount)
elif amount > balance :
    print("insufficient balance")

# else :
#     print( n = balance - amount , here it is remaining balance)
# elif n<500:
#     print("minimum balance warning" ) 
else :


shopping = int(input("enter you want shopping budget : "))
if shopping > 10000 :
    print("You have eligible 20% Discount  ")
elif 5000 <= shopping <= 9000 :
    print("10% Discount")
elif 2000 <= shopping <= 4999 :
    print("5% discount")
else :
    print("No discount available ")
if shopping < 5000:
        print("you have got free Delivery ")


marks = int(input("enter your marks : "))
income = int(input("enter your family income : "))
if 90 <= marks <= 100 and income <= 300000:
    print("grade : A")
    print("scholarship : 50%")
elif 75 <= marks <= 89 and income <= 300000:
    print("grade : B")
    print("scholarship : 30%")
elif 60 <= marks <= 74 and income <= 300000:
    print("grade : A")
    print("scholarship : NO SCHOLARSHIP")
elif 40 <= marks <= 59 :
    print("grade : C ")
else :
    print("Fail ")
    if marks < 40 :
        print('no scholarship')
"""
"""
maths = int(input("enter maths  subject marks : "))
physics = int(input("enter physics  subject marks : "))
english = int(input("enter english  subject marks : "))
hindi = int(input("enter hindi subject marks : "))
chemistry = int(input("enter chemistry subject marks : "))
totalmarks = 500

# if maths < 35 or physics < 35 or english < 35 or hindi < 35 chemistry < 35 :

obtained_marks = maths+physics+english+hindi+chemistry

percentage = (obtained_marks / totalmarks) * 100

if maths < 35 or physics < 35 or english < 35 or hindi < 35 or chemistry < 35 : 
    print("result : " , fail)


elif 90 <= percentage <= 100 :
    print("Grade A+",percentage)
elif 80 <= percentage <= 89  :
    print("Grade A" , percentage)
elif 70 <= percentage <= 79  :
    print("Grade B" , percentage)
elif 60 <= percentage <= 69  :
    print("Grade C" , percentage)
elif 50 <= percentage <= 59  :
    print("Grade D" , percentage)
else : 
    print("grade E " , percentage)








# for i in range(2,10,2):
#     print(i)

fruits = ["apple ","banana","guava","papaya"]
for fruit in fruits :
    print(fruit , end = " -->")
    
name  = "python"
for ch in name:
    print(ch)
    
dict  = {1 : "a",2 : "b",3 : "c"}
for key,values in dict.items():
    print(key,values)
    print(f" key = {key}, vaue = {values}")


names = "python"
for name in names :
    if name == "t":
        break
    # else :
    #     print(name)



p = int(input("enter a square number : "))
s = int(input("enter a number:  "))
f = s * p
print("result is : ", f)
if f % 2 == 0 :
    print("even number")
else :
    print("odd nnumber")


#n = int(input("enter a number"))
import calendar
calendar.2024
print(2024)

q = input("enter a name : ")
if q == q :
    print("names are same")
else :
    print("not same words")


n = input("enter a name : ")
palindrome

n = int(input("enter a number : "))
if n % 7 == 0 and n%11==0 :
    print("divisible by both 7 and 11")
else :
    print("not dividible by 7 and 11")

num1 = int(input("enter a num1 : "))
num2 = int(input("enter num2 : "))
num3 = int(input("enter num3 : "))
if num1 == num2 == num3:
    print("all numbers are equal")
else :
    print("all nembers are not equal")

from ast import expr


def expression():
    print("hi")
    print("hello")
def hi():
    print("welcome")


expression()
expression()
hi()

def trial():
    n = int(input("enter a number : "))
    i = int(input("enter number2 : "))
    k = n+i
    s = n * i 
    print("your addition value is : ", k)
    print("your mutiplication value is : ",s)
trial()

l1 = input("enter a letter : ")
l2= input("enter a letter : ")
l3 = input("enter a letter : ")
l4 = input("enter a letter : ")
l5 = input("enter a letter : ")
s = l1+l2+l3+l4+l5
print("all letters are combined is : ", s,"are great working")
 
a = int(input("enter a value : "))
b = int(input("enter b value : "))

c = int(input("enter c value : "))
if a + b > c and a + c > b and b + c > a :
    print("valid triangle ")
else :
    print("invalid triangle ")

n1 = int(input("enter number1 : "))
n2 = int(input("enter number2 : "))
n3 = int(input("enter number3 : "))
if n1 == n2 == n3 :
    print("all numbers are equal",n1,"=",n2,"=",n3)
elif n1 > n2 and n1 > n3 :
    print("n1 is greater than ")
elif n2 >n1 and n2 > n3 :
    print("n2 is greater")
else :
    print("n3 is greater")

for i in range(1,21) :
    if i % 2 == 0 :
        print(i,"even number")
        i = i + 1

n = 0
for i in range(1,11) :
    if   i * i  :
        print(i ,"square number")
        i = i + 1

for i in range(1,11):
    print(i,"--",i * i )

for i in range(1 , 21):
    if i % 3 == 0 :
        print(i, "this is divisible by 3")

for i in range(1 , 51):
    if i % 5 == 0 and i % 10 != 0 :
        print(i)

for s in range(1,101) :
    if s % 3 == 0 and s % 5 == 0 :
        print("BizzBuzz")
    elif s % 3 == 0 :
        print("Fizz")
    elif s % 5 == 0 :
        print("Buzz")
    else :
        print(s) 

for s in range(1,51):
    if s % 1 == 0 and s % s == 0 :
        print(s ," this is divisible by 1   and same number ")

for s in range(2,51):
    for n in range(2,s):
        if s % n == 0:
            break
    else:
        print(s)          

for i in range(1,21):
    if i % 2 != 0:
        print(i)

for i in range(1,51):
    if i % 7 == 0:
        print(i)

for i in range(1,51):
    if i % 2 == 0 and i % 4 != 0 :
        print(i)


for i in range(1,11):
    if i % 2 == 0 :
        print(i,"----->","even")
    else :
        print(i,"----->","odd")

for  i in range(1,11):
    if i **  3 :
        print("this is cube value is " , i *i* i) 


n = int(input("enter a number : "))
if n >= 0 and n <= 9 :
    print("one digit")
elif n >= 10 and n <= 99 :
    print("2 digit number")
elif n >= 100 and n <= 999 :
    print("thrree digit")
#elif n >= 1000 :
#    print("four digits")
else :
    print("four digit")

number = int(input("enter how many numbebrs you want : "))
even =0
odd = 0
for n in range(number):
    num = int(input("enter a number  : "))
    if num % 2 == 0:
        even = even + 1
       
    else :
        odd = odd + 1
print("even num is = " , even)
print("odd num is = ", odd )


n = int(input("enter how many numbers you want : "))
positiveeee = 0
negative = 0
zeero = 0
for i in range(n) :
    k = int(input("enter a number : "))
    if k > 0 :
        positiveeee =  positiveeee + 1
    elif k < 0:
        negative = negative+ 1
    else :
        zeero = zeero + 1
print("positive numbesr : ",positiveeee)
print("negative number : " , negative)
print("zeero number " , zeero)

n = int(input("enter how  many numbers : "))
even_number = 0
odd_number = 0
for i in range(n):
    num =  int(input("enter a number : "))
    if num % 2 == 0 :
        even_number = even_number + num
    else :
        odd_number = odd_number + num
print("all even numbers are added : ",even_number)
print("all odd numbers are added : ", odd_number)

for i in range(1,101):
    lastdigit = i % 10
    firstdigit = i // 10

    if firstdigit +  lastdigit == 10:
        print(i,end = " ")

for i in range(1,101):
    lastdigit = i % 10
    firstdigit = i // 10 
    digitsum = firstdigit + lastdigit
    if i % digitsum == 0:
        print(i)

for i in   range(1,101):
    if i  % 3 == 0 and i % 7 == 0 :
        print(i)

for i in range(1,1000):
    fd = i // 10 
    ld = i % 10 
    md = (i // 10 )%10
    if fd == ld :
        print(i) 
    else: 
        print(i,"this is not same number")   

p = input("enter a letter : ")
n = p[::-1]
if p==n:
    print("palindrome")
else :
    print("not palidrome")  
n = int(input("enter how many letters you want : "))
for i in range(n) :
    k = input("enter a letter : ")
    s = k[::-1] 
    if k == s :
        print(f"your word {k} is plindrome ")
    else :
        print("not palindrome")   

ascii.__class__

n = int(input("enter a number : "))
if n % 2 == 0 :
    print("this is even number : " , n)
else :
    print("this is odd number : ",n)

n = int(input("enter a number"))
for i in range(n):
    num =  int(input("enter a number : "))

    lastdigit = i // 10
    middledigit = (i // 10 ) % 10
    firstdigit = i % 10
    #lastdigit as ld
    if firstdigit == lastdigit == middledigit:
        print("all numbers aere same ") 
    else : 
        print("not same")
n= input("enter how many numbers :  ")
count = 0
k=0
for i in n:
    if int(i) % 2 == 0 :
        count = count+1 
        k = k + int(i)
print("Even number count = ",count)
print(k)

n = input("enter a number  : ")
first = n[0]
same = True

for i in n:
    #if i == i == i ==i :
    if i != first :
        same = False 

if same :
    print("all numbers are same")
else :
    print("not all numbwrs arew same")
        
      #  print("all are saame ")
    #else :
    #    print("allare not saaaaeme")

n = input("enter a number : ")
for i in n:
    if i == "0":
        print("zero is present")
    else :
        print("zero is not prresent")

n = input("enter a number : ")
for i in n :
    if i == 

def even():
    n = int(input("enter a number : "))
    if n % 2 == 0 :
        print("even number : ",n)
    else :
        print("odd number",n)
even()

def h(a,b):
    print(a+b,"addition")
h(5,4)
h(4,9)

n = int(input("enter how many leters : "))
for i in range(n):
    s = input("give me letter : ")
    a = s[::-1]
if s == a:
    print("given letter is palindrome")
else :
    print("given letter is not palindrsome")
    #print(a)

for i in range(1,5):
    for i in j:
        print("*")

for i in range(1,5):
    for s in range(1,i+1):
        print("*",end =" ")
    print()     

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end= " ")
    print()                                         

s = 0 
for i in range(1,5):
    for j in range(1,i+1):
        s = s+1
        print(s,end=" ")
    print()

for i in range(1,5):
    for j in range(1,i + 1):
        print("*",end = " ")
        #print(end = " ")
    print()  
for i in range(3,0, -1):
    for j in range(1 ,i + 1):
        print(i,end = " ")  
    print()  

for i in range(1,5):
    #spaces
    for j in range(1 , 5 - i):
        print(" " , end = " ")
    # stars
    for j in range(1,2*i):
        print(i, end = " ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        if j <= i:
            print(j,end = " ")
    print()

for i in range(1,10):
    print(str(i) * i)
print()

for i in range(1,6):
    for j in range(1,i + 1):
        if j <= i :
            print("*",end="")
        else:
            pass
    print()    

sum = 0
for i in range(1,11):
    sum = sum + i
    print(sum)

largest = 0
numbers = [12,45,7,89,34,23,100,999]
for i in numbers:
    if i > largest:
        largest = i
print(largest)

n = int(input("enter a number : "))
k = 0
#l = 0
while n > 0:
    digit = n % 10
    k = k * 10 + digit
    #l = l + k
    n = n // 10
print(k)

for i in range(1,6):
    for s in  range(1,i + 1):
        print("*",end = "")
    print()

num = 1
row = 1
while row <= 5:
    c = 1
    #
    while c <= row :
        print(num, end = " ")
        num = num + 1
        c = c + 1
    print()
    row = row + 1  

n = int(input("enter a number : "))
if n % 2 == 0 :
    print(n,"this is even number")
else :
    print(n,"is odd nume]ber ")

n = int(input("enter a number"))
s = 0 
k = 0
for i in range(1 ,n):
    if i % 2 == 0:
        s = s + i
    else :
        k = k + 1
print(s,"this is sum")
print(k,"this is how many numbres")

sum = 0
count = 0
for i in range(1,101):
    if i % 2 == 0:
        sum = sum + i
    else:
        #i % 5== 0

        count = count + i
difference = sum - count
print("sum of divisible by 3 = " ,sum)
print("count of not divisible by 3 = ",count) 
print("difference = ",difference)
#divisible  by 15
sum = 0 
count = 0 
for i in range(1,101):
    #if i % 3 == 0 and i % 5 == 0 :
    while i % 15 == 0:
        sum = sum + i
    #else :
        count = count + 1 
        break
print("sum is = ", sum)
print("count is = ",count)

sum = 0
count = 0
for i in range(1,101):
    if i % 2 != 0 and i % 3 == 0:
        sum = sum + i
        count = count + 1
print("sum is = ",sum)
print("count is = ",count)

sum = 0
count = 0 
largest = 0
for i in range(1,101):
    if i % 4 == 0:
        sum = sum + i
        count = count + 1
        if largest < i:
            largest = i
print("sum is = ",sum)
print("count is = ",count)
print("largest is = ",largest)            

sum = 0 
count = 0
for i in range(1,101):
    if i % 3== 0 and i % 5 != 0:
        sum += i
        count += 1
print("sum is = ",sum)
print("count is = ",count)

sum = 0 
count = 0
for i in range(1,101):
    if i % 2== 0 or i % 5 == 0:
        sum += i
        count += 1
print("sum is = ",sum)
print("count is = ",count)

n = int(input("enter a number : "))
sum = []
count = 0
while n > 0:
    digit = n % 10
    if digit % 2== 0:
        sum.append(digit)
    n = n // 10
for digit in sum :
    count = count + 1
total = 0
for digit in sum :
    total = total + digit
print("even digits count : ",count)
print("even digits sum : ",total)

n = int(input("enter a number : "))
sum = 0
count = 0
for i in range(1,n):
    if i % 3 == 0:
        sum = sum + i
        count = count +    1
print("sum = ",sum)
print("count = ",count)



sum = 0
count = 0
n = int(input("enter a number : "))
for i in range(1,n):
    if i % 3 == 0 and  i % 2 != 0:
        sum = sum + i
        count = count + 1
print(sum)
print(count) 

n = int(input("enter a number : "))
sum = 0
count = 0
for i in range(1 , n+1):
    if i ** 0.5 == int(i ** 0.5):
        sum = sum + i
        count = count + 1
print("sum : ",sum)
print("count : ",count) 

n = int(input("enter a number : "))
sum = 0 
count = 0
for i in range(1,n):
    if i % 5 == 0 :
        if i % 10 != 0:
            sum = sum + i
            count = count + 1
print(sum)
print(count)

n = int(input("enter a number : "))
sum = 0 
count = 0
for i in range(1,n+1):
    if i % 9 == 0 :
        if i > 50 :
            if i % 5 != 0:
                sum = sum + i
                count = count + 1
print(sum)
print(count)

n = int(input("enter a letter : "))
for i in range(1,n):

count = 0
for i in range(1,16):
    if i % 2 == 0:
        if i % 4 == 0:
            count = count + 2
        else :
            count = count + 1
print(count)


def add():
    a = int(input("ennter  a value : "))
    b = int(input("ennter  b value : "))
    n = a+b
    #print("a+b value is",a + b )
    print("a + b value is = ", n)


    if n % 2 == 0 :
        print("even number = ",n)
    else :
        print("odd number = ",n)
add()
add()

f = input("enter a letter : ")
t = 0
list = ["apple","papaya","fee","threat","payment","fee","pay instantly"]
for i in list:
    if f == i :
        t = t + 1
        print(f)
        print(t)
        if t == 2:
            print("threat level is 70 %")
        elif t == 1:
            print("thtreat levl is 50 %")
        if f != i:
            print("no threat is available")
        #else :
            #print("no threat level")

#n   = int(input("enter the number : "))
for i in range(1,40):
    if i % 2 != 0:
        
        print(i)
    #else :
     #   print("this is odd number : ",i)


c = 0 
for i in range(1,21):
    if i % 3 == 0 :
        c = c + 1
print(c)

sum = 0
for  i in range(1,31):
    if i % 5 == 0 :
        sum = sum + i
print(sum)

sum = 0
count = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 != 0:
        sum = sum + i
        count = count + 1
print(count)

number = int(input("enter a number : "))
count = 0
sum =0
numbers = str(number)
for i in numbers :
    if int(i) % 2 == 0 :
        count = count + 1
        sum = sum + int(i)
print(count)
print(sum)

number = int(input("enter a number : "))
count = 0
sum =0
numbers = str(number)
for i in numbers :
    if int(i) % 2 == 0 :
        count = count + 1
    else :
        count  = count + 1
        #sum = sum + int(i)
print(count)
print(count)

k = 0
maths = int(input("enter maths marks : "))
physics = int(input("enter physics marks : "))
social = int(input("enter social marks : "))
if maths < 35 and physics < 35 and social < 35 :
    print("failed")
    if maths < 35 :
        print("mathss failed : ",maths)
    elif physics < 35:
        print("physics is failed : ",physics)
    else :
        print("social failed",social)


k = (maths + physics + social) / 3
print("total percentage is :",k)
"""


     
    
                        




























































































































































































































































































































