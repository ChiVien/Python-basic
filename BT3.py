# n=int(input('nhap n: '))
# def dao(n):
#     n=int(str(n)[::-1])
#     print(n)
# dao(n)

# def tinhgiaithua(n):
#     giai_thua = 1
#     if (n == 0 or n == 1):
#         return giai_thua
#     else:
#         for i in range(2, n + 1):
#             giai_thua = giai_thua * i
#         return giai_thua
 
# n = int(input("Nhập số nguyên dương n = "))
# print("Giai thừa của", n, "là", tinhgiaithua(n))

# def tinhtong(n):
#     x=0
#     for i in range(n+1):
#         x+=i**3
#     return x 
# n=int(input('nhap n: '))
# print('tong =',tinhtong(n))

# def tongle(n):
#     x=0
#     for i in range(n+1):
#         if (i%2!=0):
#             x+=i
#     return x
# n=int(input('nhap n: '))
# print('tong so le la:',tongle(n))

# def tongle(n):
#     x=0
#     for i in range(n+1):
#         if (i%2==0):
#             x+=i
#     return x
# n=int(input('nhap n: '))
# print('tong so chan la:',tongle(n))

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

# def sochinhphuong(n):
#     if n<4:
#         print(f"{n} khong la so chinh phuong")
#     for i in range (int(math.sqrt(n))+1):
#         if i*i==n:
#             print(f"{n} la so chinh phuong")
#         elif i*i >n:
#             print(f"{n} khong la so chinh phuong")
#             break
# n=int(input("Nhap n:"))
# sochinhphuong(n)

# def tongsnt(n):
#     s=0
#     for i in range(1,n+1):
#         if snt(i):
#             s+=i
#     print(f"Tong cac so nguyen to: {s}")
# n=int(input("Nhap n:"))
# tongsnt(n)

# def bang9chuong(n):
#     for i in range(1,11):
#         print(f"{i}*{n}={i*n}")
# n=int(input("Nhap n:"))
# bang9chuong(n)

# def fibo(n):
#     "Ham tinh so fibonacci"
#     if n==1 or n==2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# n=int(input("Nhap n:"))
# print(f"So fibo thu {n}: {fibo(n)}")