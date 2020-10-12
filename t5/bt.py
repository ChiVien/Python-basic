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
def tinhtich(n):
    arr=[]
    for i in range(n):
        arr.append(int(input(f'input Item[{i+1}]')))
    tich=0
    for i in range(n):
        tich+=arr[i]
    return tich
n=int(input(f'nhap N: '))
print(tinhtich(n))