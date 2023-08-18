
# #ASSIGNMENT 3

# #Q1 WRITE A PYTHON PROGRAM TO PRINT THE FOLLOWING STRING IN A SPECIFIC FORMAT
# print('Twinkle,twinkle,little star,')
# print('\tHow I wonder what you are!')
# print('\t\tUp above the world so high,')
# print('\t\tLike a diamond in the sky.')
# print('Twinkle,twinkle,little star,')
# print('\tHow I wonder what you are!')

# print('\n\n')
# #Q2 WRITE A PYTHON PROGRAM TO GET THE PYTHON VERSION YOU ARE USING
# import sys
# print('PYTHON VERSION: ',sys.version)

# #Q3 WRITE A PYTHON PROGRAM TO DISPLAY THE CURRENT DATE AND TIME
# import datetime
# dat= datetime.datetime.now()
# print('CURRENT DATE & TIME: ', dat.strftime('%d/%m/%Y %H:%M:%S'))

# #Q4 WRITE A PYTHON PROGRAM WHICH ACCEPTS THE RADIUS OF A CIRCLE FROM THE USER AND COMPUTE THE AREA
# import math #To use pi value
# pi=math.pi
# r=int(input('Enter Radius: '))

# print('PI = ',round(pi,3),'\nRADIUS = ',r)

# #calculating area
# area=pi*math.pow(r,2)
# print('AREA OF A CIRCLE: ', round(area,))

# #Q5 WRITE A PYTHON PROGRAM WHICH ACCEPTS THE USER'S FIRST NAME AND LAST NAME & PRINT THEM IN REVERSE ORDER WITH A SPACE IN BETWEEN THEM.
# first_name=input('FIRST NAME: ')
# last_name=input('LAST NAME: ')
# full_name=first_name+' '+last_name

# print('ORIGINAL: ',full_name)

# a = full_name.split()      #using split method to split at whitespaces
# a.reverse()     #reversing all the elements of the string 
# print('REVERSED: ','  '.join(a))    #concatenate them into a string

# #Q6 WRITE A PYTHON PROGRAM WHICH TAKES TWO INPUTS FROM USER AND PRINT THEM ADDITION
# a=int(input('1ST NUMBER: '))
# b=int(input('2ND NUMBER: '))
# addition=a+b
# print('ADDITION: ',addition)


# #Q7 WRITE A PROGRAM WHICH TAKES 5 INPUTS FROM USER FOR DIFFERENT SUBJECT'S MARKS, TOTAL IT & GENERATE MARK SHEET USING GRADES
# #Taking input marks of Eng,Isl and Maths Out Of 100
# eng=int(input('Enter Your English Marks: '))
# isl=int(input('Enter Your Islamiat Marks: '))
# maths=int(input('Enter Your Maths Marks: '))
# science=int(input('Enter Your Science Marks: '))
# urdu=int(input('Enter Your Urdu Marks: '))

# if eng< 0 or eng>100 or isl>100 or isl<0 or maths>100 or maths <0 or science>100 or science<0 or urdu>100 or urdu<0 :    #Check for whether the marks are
#     print('Wrong Input.. Marks should be in between 1-100')
# else:
#     #Variable storing total marks
#     Total_marks=500

#     #Calculating percentage
#     perc=((eng+isl+maths+science+urdu)/Total_marks)*100
#     print('\nPercentage = ', round(perc,2), '%')


#     #Calculating grade
#     if perc<=100 and perc>=80:
#         print('Grade = A+')
#     elif perc<80 and perc>=70:
#         print('Grade = A')
#     elif perc<70 and perc>=60:
#         print('Grade = B')
#     elif perc<60 and perc>=50:
#         print('Grade = C')   
#     elif perc<50 and perc>=40:
#         print('Grade = D')
#     elif perc<40 and perc>=33:
#         print('Grade = E')
#     elif perc<33 and perc>=0:   
#         print('Grade = Fail')
#     else:
#         print('Error 101..Please Enter Correct Percentage')

# #Q8 WRITE A PROGRAM WHICH TAKE INPUT FROM USER AND IDENTIFY TAHT THE GIVEN NUMBER IS EVEN OR ODD
# x=int(input('ENTER NUMBER: '))
# if(x%2==0):     #if remainder = 0 when divided by 2, then it must be an even number
#     print(x, 'IS AN EVEN NUMBER')
# else:
#     print(x, 'IS AN ODD NUMBER')

# #9. Write a program which print the length of the list?
# list=[10,20,'S','SAMIYA',10.25,'WAJIHA',30,40]
# print('THE LENGTH OF THE LIST',list,' = ',len(list))

# #10.Write a Python program to sum all the numeric items in a list?
# list=[10,20,'S','SAMIYA',10.25,'WAJIHA',30,40]
# numeric_list=[]
# sum=0
# for a in list:
#     if(isinstance(a,(int,float))):
#         sum+=a
#         numeric_list.append(a)
# print('THE SUM OF ALL NUMERIC VALUES',numeric_list,'IN THE LIST',list,' = ',sum)
    

# #11.Write a Python program to get the largest number from a numeric list.
# numeric_listlist=[10,20,10.25,30,40]
# largest=max(numeric_list)
# print('THE LARGEST NUMBER IN A NUMERIC LIST',numeric_list,'IS',largest)
    

# #12. Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# #Write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print('ELEMENTS OF THE LIST',a, 'LESS THAN 5 ARE FOLLOWING: ')
# for i in a:
#     if(i<5):
#         print(i)

