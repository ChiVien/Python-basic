import math
"""
BT1: tim max min
"""
# def max_min(*numbers):
#     print(f"Day duoc truyen vao: {numbers}")
#     max=min=numbers[0]
#     for number in numbers:
#         if number<min:
#             min=number
#         elif number>max:
#             max=number
#     print(f"Max: {max} | Min: {min}")
# max_min(100,3,5,10,1,20,30,299,80,50,40,2,4)

"""
BT2: Chuoi nghich dao
"""
# def reverse_string(str):
#     str=str[::-1]
#     return str
# str=input("Nhap chuoi: ")
# print(f"Chuoi nghich dao: {reverse_string(str)}")
"""
BT3: Kiem tra so hoan hao
"""
# def is_perfect(n):
#     s=0
#     if(n<=0):
#         return False
#     for i in range(1, n//2+1):
#         if n%i==0:
#             s+=i
#     if s==n:
#         return True
#     else:
#         return False
# n=int(input("Nhap so muon kiem tra: "))
# if is_perfect(n):
#     print(f"{n} la so hoan hao")
# else:
#     print(f"{n} khong la so hoan hao")
"""
BT4: Kiem tra so nguyen to
"""
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return False
#     return True
# n=int(input("Nhap so: "))
# if is_prime(n):
#     print(f"{n} la so nguyen to")
# else:
#     print(f"{n} khong la nguyen to")
"""
BT5: Dem so luong chu hoa, chu thuong
"""
# def count_upper_lower(str):
#     upper=lower=0
#     for i in str:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#     print(f"So luong chu hoa: {upper}|So luong chu thuong: {lower}")
# str=input("Nhap chuoi muon dem: ")
# count_upper_lower(str)
"""
BT6: Kiem tra chuoi pangram
"""
# def is_pangram(str, alphabet):
#     for char in alphabet:
#         if char not in str.lower():
#             return False
#     return True
# str=input("Nhap chuoi muon kiem tra: ")
# alphabet="abcdefghijklmnopqrstuvwxyz"
# if is_pangram(str,alphabet):
#     print(f" \"{str}\" la chuoi pangram")
# else:
#     print(f" \"{str}\" khong la chuoi pangram")

"""
BT7: Tao ma tran
"""
# def create_matrix(n,m):
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             print(i*j,end="\t")
#         print()
# n=int(input("Nhap so hang: "))
# m=int(input("Nhap so cot: "))
# create_matrix(n,m)
"""
BT9: Chuyen hoa thanh thuong va nguoc lai
"""
# def change_upper_lower(str):
#     str=str.swapcase()
#     print(f"Chuoi sau khi chuyen: {str}")
# str=input("Nhap chuoi muon chuyen: ")
# change_upper_lower(str)
"""
BT10: De quy dem so luong chu so le
"""
# i=0
# def count_odd(n,i):
#     if i==len(n) or n[i].isnumeric==False:
#         return 0
#     if int(n[i])%2!=0:
#         return 1+count_odd(n,i+1)
#     else:
#         return 0+count_odd(n,i+1)
# n=input("Nhap so can kiem tra: ")
# print(count_odd(n,i))    

