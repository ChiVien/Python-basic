"""
BT1/a
"""
# def tinhtong(n):
#     arr=[]
#     for i in range(n):
#         arr.append(int(input(f'input Item[{i+1}]')))
#     tong=0
#     for i in range(n):
#         tong+=arr[i]
#     return tong
# n=int(input(f'nhap N: '))
# print(tinhtong(n))

"""
BT1/b
"""  
# def tinhtich(n):
#     arr=[]
#     for i in range(n):
#         arr.append(int(input(f'input Item[{i+1}]')))
#     tich=1
#     for i in range(n):
#         tich*=arr[i]
#     return tich
# n=int(input(f'nhap N: '))
# print(tinhtich(n))
"""
BT1/c,d
"""  
# def max_min(n):
#     arr=[]
#     for i in range(n):
#         arr.append(int(input(f'input Item[{i+1}]')))
#     max=min=arr[0]
#     for i in range(n):
#         if arr[i]<min:
#             min=arr[i]
#         elif arr[i]>max:
#             max=arr[i]
#     print(f"Max: {max} | Min: {min}")
# n=int(input(f'nhap N: '))
# max_min(n)
"""
BT1/e,f
"""  
# def chanle(n):
#     arr=[]
#     for i in range(n):
#         arr.append(int(input(f'input Item[{i+1}]')))
#     chan=[]
#     le=[]
#     for i in range(n):
#         if arr[i]%2==0:
#             chan.append(arr[i])
#         elif arr[i]%2!=0:
#             le.append(arr[i])
#     print(f'so chan {chan}| so le {le}')
# n=int(input(f'nhap N: '))    
# chanle(n)
"""
BT1/g
"""
import math

# def tongsnt(n):
#     arr=[]
#     for i in range(n):
#         arr.append(int(input(f'input Item[{i+1}]')))
#     snt=[]
#     for i in range(n):
#         if arr[i]<=1:
#             continue
#         for j in range(2,100):
#             if arr[j]%arr[i]==0:
#                 continue
#         else:
#             snt.append(int(arr[i]))
#     tong=0
#     for i in range(len(snt)):
#         tong+=snt[i]
#     return tong
# n=int(input(f'nhap N: '))
# print(tongsnt(n))
"""
BT2
"""
