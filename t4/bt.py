"""
Cao Dương Chí Viễn 
13THC
1906020140
"""
"""
BT1: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
"""
# def thaydoi():
#     a=input('nhap chuoi: ')
#     s=a[0]
#     for i in range(1,len(a)):
#         if a[i]==a[0]:
#             s+="$"
#         else:
#             s+=a[i]
#     return s
# print(f'chuoi: {thaydoi()}')
"""
BT2: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
"""
# def xoakitu():
#     a=input('nhap chuoi: ')
#     m=int(input('nhap so thu tu : '))
#     s=a[0]
#     while m<0:
#         m=int(input('nhap lai: '))
#     return a[:m-1] + a[m:]
# print(f'xuat chuoi: {xoakitu()}')
"""
BT3: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
"""
# def xoakitule():
#     a=input('nhap chuoi: ')
#     return a[::2]
# print(f'xuat chuoi: {xoakitule()}')
"""
BT4: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
"""
# def inkitu(s):
#     return s[0:2] + s[-3:-1] if len(s)>1 else " "
# s=input("Nhap chuoi: ")
# print(f"Chuoi moi: {inkitu(s)}")
"""
BT5: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
"""
# print("Tim ky tu max, min")
# def max_min(s):
#     max=min=s[0]
#     for char in s:
#         if max < char:
#             max = char
#         if min > char:
#             min = char
#     return max,min
# s=input("Nhap chuoi: ")
# max,min=max_min(s)
# print(f"Ky tu lon nhat: {max}| Ky tu nho nhat: {min}")

"""
BT6: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
"""
# print("nhap chuoi: ",end="")
# s=str(input())
# def hoa(s):
#     kq1=""
#     for i in s:
#         if i.islower():
#             kq1+=i.upper()
#         else:
#             kq1+=i.lower()
#     return kq1
# print(f"Hoa: {hoa(s)}")
