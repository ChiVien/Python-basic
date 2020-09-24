## giải phương trình bậc 2 
"""
# Giải phương trình bậc 2: ax2 + bx + c = 0
# @param a: hệ số bậc 2
# @param b: hệ số bậc 1
# @param c: số hạng tự do
"""
import math
from fractions import *
# def giaiPTBac2(a, b, c):
#     if (a == 0):
#         if (b == 0):
#             print ("Phương trình vô nghiệm!")
#         else:
#             print ("Phương trình có một nghiệm: x = ", + (-c / b))
#     DT=b*b-4*a*c
#     if DT>0:
#         x1 = (float)((-b + math.sqrt(DT)) / (2 * a))
#         x2 = (float)((-b - math.sqrt(DT)) / (2 * a))
#         print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
#     elif DT==0:
#         x1 = (-b / (2 * a))
#         print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
#     else:
#         print("Phương trình vô nghiệm!")

# print('Nhap a: ',end='')
# a=float(input())
# print('Nhap b: ',end='')
# b=float(input())
# print('Nhap c: ',end='')
# c=float(input())
# giaiPTBac2(a, b, c)
"""
Giải phương trình: S1=1+x+x^2+x^3+...+x^n
"""
# print('Nhap X: ',end='')
# x=int(input())
# print('Nhap n: ',end='')
# n=int(input())
# S1=0
# if (n==0):
#     S1=1
#     print('KQ= ',S1)
# else:
#     for i in range(n+1):
#         S1=S1+pow(x,i)
#     print('KQ= ',S1)
"""
Giải phương trình: S2=1-x+x^2-x^3+...+(-1)^n*x^n
"""
# print('Nhap X: ',end='')
# x=int(input())
# print('Nhap n: ',end='')
# n=int(input())
# S2=0
# if (n==0):
#     S2=1
#     print('KQ= ',S2)
# else:
#     for i in range(n+1):
#         S2=S2+pow(-1,i)*pow(x,i)  
#     print('KQ= ',S2)
"""
Giải phương trình: S3=1+(x/1!)+(x^2/2!)+...+(x^n/n!)
"""
# print('Nhap X: ',end='')
# x=int(input())
# print('Nhap n: ',end='')
# n=int(input())
# S3=0
# if(n==0):
#     S3=1
#     print('KQ= ',S3)
# else:
#     for i in range(1,n+1):
#         S3=S3+Fraction(pow(x,i),i)
#     print('KQ= ',S3)
"""
Lập Chương Trình BT3
"""    
# S4=0
# n=int(input('Nhap n: '))
# while n>1000:
#     n=int(input('Nhap Lai: '))
# for i in range(n+1):
#     S4=S4+i
# print('KQ= ',S4)
"""
Lập Chương Trình BT4
"""
# print('Nhap a: ',end='')
# a=int(input())
# print('Nhap b: ',end='')
# b=int(input())
# print('Nhap c: ',end='')
# c=int(input())
# if ((a+b>c)| (a + c > b)|(b + c > a)):
#     print("Đây là tam giác !")
#     if ((a * a == b * b + c * c) | (b * b == a * a + c * c) | (c * c == b * b + a * a)):
#         print("Đây là tam giác vuông !")
# else:
# 	print("Đây không phải tam giác")

