# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

# itration for number

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# print (students)
# for i in range(0,len(students)):
#     print(students[i][1])

#####################################################################################################
# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# students = ['Prashant',32],['Pallavi',36],['Dheeraj',39],['Shivam',40]
# name,scores =  input('Enter name:'),int(input('Enter Score: '))
# n = int(input("Enter no of inputs = ", ))
# students = []
# for x in range(0, n):
#     l = []
#     name = input()
#     score = float(input())
#     l.append(name)
#     l.append(score)
#     students.append(l)
# # print(students)
#
# result = 9999999
# final= 99999
# for i in range(0,len(students)):
#     # print(students[i][1])
#     if students[i][1] < result:
#         # print(students[i][1], result, students[i][1] < result)
#         final = result
#         result = students[i][1]
#     elif students[i][1] < final:
#         # print(students[i][1], final, students[i][1] < final)
#         final = students[i][1]
# # print(result)
# # print(final)
# s = []
# for j in range(0,len(students)):
#     if students[j][1] == final:
#         # print(students[j][0])
#         s.append(students[j][0])
# s.sort()
# for k in s :
#     print(k)

# set(students[j][0])
# print(students[j][0])


# L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
# print(L[2])
# # Prints ['cc', 'dd', ['eee', 'fff']]
# print(L[2][2])
# # Prints ['eee', 'fff']
# print(L[2][2][0])
# # Prints eee




#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# dic = {}
# s = list()
# for k in range(int(input())):
#     name = input()
#     score = float(input())
#     if score in dic:
#         dic[score].append(name)
#     else:dic[score]=[name]
#     if score not in s:
#         s.append(score)
# m = min(s)
# s.remove(m)
# m1=min(s)
# dic[m1].sort()
# for i in dic[m1]:
#     print(i)

# ################################################################################################################

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# n = int(input("Enter no. of input = "))
# dic = {}
# for i in range(0,n):
#     key = input()
#     l = []
#     for i in range(0,3):
#         value = float(input())
#         l.append(value)
#     print(l)
#     dic[key] = l
# print("Final input Dictionary",dic)
# x = input("enter name of student = ")
# y=dic[x]
# z =sum(y)/len(y)
# print("{:.2f}".format(z))

###################################################################################################################

# N = int(input("number of input = "))
# l=[]
# for i in range(0,4):
#     q = int(input("enter place = "))
#     w = int(input("enter number = "))
#     l.insert(q,w)
# print(l)
# l.pop(0)
# print(l)
# z = int(input("enter no add at last = "))
# l.append(z)
# print(l)
# print()
# l.sort()
# print("sorted list  = ",l)
# l=l[:-1]
# print(l)
# l.reverse()
# print("final ",l)

# N = int(input("number of input = "))
# output = []
# for i in range(0, 4):
#     x = input().split()
#     if x[0]=="print":
#         print(output)
#     elif x[0] == "insert":
#         output.insert(int(x[1],int(x[2])))
#     elif x[0] == "remove":
#         output.remove(int(x[1]))
#     elif x[0] == "pop":
#         output.pop()
#     elif x[0] == "append":
#         output.append(int(x[1]))
#     elif x[0] == "sort":
#         output.sort()
#     else:
#         output.reverse()

##################################################################################################################
# n = int(input())
# integer_list = map(int, input().split())
# t = tuple(integer_list)
# print(hash(t))

################################################################################################################
# import operator
# s = input()
# new ={}
# for i in s:
#     if i in new:
#         new[i] += 1
#     else:
#         new[i] = 1
# sd = sorted(new.items(),key=operator.itemgetter(1),reverse=True)
# # print(str(new))
# # print(str(sd))
# for x in range(0,3):
#     # if x[1]>=2:
#     print(x[0],x[1])
# -----------------------------------------------------------------------------------------------
# from collections import Counter
# s = sorted(input())
# count = Counter(s)
# # print(count)
# count = Counter(s).most_common(3)
# # print(count)
# for x in count:
#     print(*x)

# ###################################################################################################
# def swap_case(s):
#     s = input()
#     output = ""
#     for char in s :
#         if(char.islower()== True):
#             output += (char.upper())
#         elif (char.isupper() == True):
#             output += (char.lower())
#         else:
#             output += char

# return output
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# #################################################################################################################
# x = int(input("enter no. of input = "))
# # s = []
# for i in range(x):
#     num = input()
#     if len(num)>10 or len(num)<10:
#         print("NO")
#     elif num[0] == '7' or num[0] == '8' or num[0] == '9':
#         try:
#             num = int(num)
#             print("YES")
#         except:
#             print("NO")
#     else:
#         print("NO")

# ##################################################################################################################

# a = input()
# b = a.split(" ")
# # print(b)
# b = '-'.join(b)
# print(b)

# ###################################################################################################################
# x = input("Enter your First name = ")
# y = input(" enter your last name = ")
# a = ("Hello {0} {1}! You just delved into python.").format(x,y)
# print(a)

# ###################################################################################################################
# s = "abcdefgh"
# l = []
# for i in s:
#     l.append(i)
# print(l)
# for k in l:
#     x = int(input("place = "))
#     y = input("word = ")
#     l[x] = y
#     s = ''.join(l)
#     print(s)
#
# def mutate_string(s, x, y):
#     l = []
#     for i in s:
#         l.append(i)
#     l[x] = y
#     s = ''.join(l)
#     print(s)
#
# s = input()
# x = int(input("place = "))
# y = input("word = ")
# mutate_string(s, x, y)

# ################################################################################################################

# def count_substring(string, sub_string):
#     x = 0
#     # ctr = 0
#     # for i in range(len(string)):
#     #     if(string[i] == sub_string[0]):
#     #         flag = True
#     #         for j in range(len(sub_string)):
#     #             if(i+j>=len(string)):
#     #                 flag = False
#     #                 break
#     #             else:
#     #                 if string[i+j] != sub_string[j]:
#     #                     flag = False
#     #                     break
#     #         if flag:
#     #             ctr += 1
#     # return ctr
#     for i in range(len(string)):
#         if string.startswith(sub_string,i):
#             x += 1
#     return x
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)



# ###################################################################################################################

# s = input()
# print(any([i.isalnum()for i in s]))
# print(any([i.isalpha()for i in s]))
# print(any([i.isdigit()for i in s]))
# print(any([i.islower()for i in s]))
# print(any([i.isupper()for i in s]))

####################################################################################################################

# n = int(input("enter the number of rows = "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")                               #Triangle code
#     for j in range(2*i+1):
#         print("H",end=" ")
#     print()


#/##################################################################################################################
# import textwrap
#
# def wrap(string, max_width):
#     x =(textwrap.fill(string,max_width))
#     return x
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# ######################################################################################################################



# _______________________________________________________________________________________________________________
# for i in range(0,5):
#     for j in range(0,5):
#         if i == j:
#             print("*", end =" ")
#         else:
#             print(" ",end=" ")
#     print("")

# n = int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if i+j == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# n = int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if i+j == n-1 or i == j :
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print("")


# n = int(input())
# x = n // 2
# print(x)
# for i in range(0,n):
#     for j in range(0,n):
#        if (i == x) or (j == x):
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print("")


# for i in range(0,10):
#     for j in range(i):
#         print("*",end="")
#     print("")


# x = int(input())
# for i in range(0,x):
#     for j in range(0,x):
#         if i+j >= x-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# n = int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if i+j <= n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# ##############################################################################################################

# x,m = list(map(int,input().split()))
# s2 = "WELCOME"
# # if x % 2 != 0:
# #     # print(x,end=' ')
# #     m = x*3
# # print(m)
# for i in range(x//2):
#     pattern = ".|."*((2*i)+1)
#     print(pattern.center(m,"-"))
# print(s2.center(m,"-"))
# for i in range(x//2-1,-1,-1):
#     pattern = ".|."*((2*i)+1)
#     print(pattern.center(m,"-"))

# ###################################################################################################################


# l1 = len(bin(number)[2:])
#
# for i in range(1, number + 1):
#     print(str(i).rjust(l1, ' '), end=" ")
#     print(oct(i)[2:].rjust(l1, ' '), end=" ")
#     print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
#     print(bin(i)[2:].rjust(l1, ' '), end=" ")
#     print("")

# ###################################################################################################################

#example---------------------------
# m=6
# for i in range(65,70):
#     m=m-1
#     for j in range(m,1,-1):
#         print(" ",end="")
#     for k in range(65,i+1):
#         print(chr(k),end="")
#     for n in range(65,i):
#         print(chr(n),end="")
#     print()


# def rangoli(size):
#     n = size
#     l1 = list(map(chr,range(97,123)))
#     x = l1[n-1::-1]+l1[1:n]
#     m = len("-".join(x))
#     for i in range(1,n):
#         print("-".join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,"-"))
#     for i in range(n,0,-1):
#         print("-".join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,"-"))
# if __name__ == '__main__':
#     n = int(input())
#     rangoli(n)


# ############################################################################################################
def mg (string):
    p1 = 0
    p2 = 0
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            p1 = p1 + (str_len) - 1
