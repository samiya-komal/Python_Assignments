#ASSIGNMENT4
#1. Make a calculator using Python with addition , subtraction , multiplication ,division and power.
print('---------------CALCULATOR--------------')
a=int(input('1ST NUMBER: '))
b=int(input('2ND NUMBER: '))
operator=input('\nENTER OPERATOR ( + , - , * , / , POWER ): ').upper()
addition=a+b
subtraction=a-b
multiplication=a*b
division=a/b
power=pow(a,b)
if(operator=='+'):
    print('ADDITION: ',addition)
elif(operator=='-'):
    print('SUBTRACTION: ',subtraction)
elif(operator=='*'):
    print('MULTIPLICATION: ',multiplication)
elif(operator=='/'):
    print('DIVISION: ',division)
elif(operator=='POWER'):
    print(a,' POWER ',b, ': ' ,power)
else:
    print('INVALID OPERATOR...')
    
#2. Write a program to check if there is any numeric value in list using for loop.
list=[10,20,'S','SAMIYA',10.25,'WAJIHA',30,40]
numeric_list=[]
count=0
for a in list:
    if(isinstance(a,(int,float))):
        count+=1
        numeric_list.append(a)
print('THERE ARE ',count,' NUMERIC VALUES IN THE LIST: ',numeric_list,)
    
#3. Write a Python script to add a key to a dictionary.
dictionary={
    'key1':"SUN",
    'key2':"MOON",
    'key3':"STARS"
}
dictionary['key4']="EARTH"
print(dictionary)

#4. Write a Python program to sum all the numeric items in a dictionary.
list=[10,20,'S','SAMIYA',10.25,'WAJIHA',30,40]
numeric_list=[]
sum=0
for a in list:
    if(isinstance(a,(int,float))):
        sum+=a
        numeric_list.append(a)
print('THE SUM OF ALL NUMERIC VALUES',numeric_list,'IN THE LIST',list,' = ',sum)
    

#5. Write a program to identify duplicate values from list.
list=[10,20,30,10,40,20,40,50]
list1=[]
list2=[]
for a in list:
    if a not in list1:
        list1.append(a)
    else:
        list2.append(a)

print('DUPLICATE VALUES IN THE LIST',list,'ARE FOLLOWING: ',list2)

#6. Write a Python script to check if a given key already exists in a dictionary
dictionary={
    'key1':"SUN",
    'key2':"MOON",
    'key3':"STARS"
}
def is_exist(a):
    if a in dictionary:
       print('KEY IS ALREADY EXIST..')
    else:
       print('KEY DOES NOT EXIST..')

is_exist('key1')
is_exist('key4')




