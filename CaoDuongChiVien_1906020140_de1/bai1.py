'''
BT1:
Tạo mảng a = [1, 1, 2, 5, 7, 9]

Thay thế phần tử đầu tiên là 0. (Kết quả: a = [0, 1, 2, 5, 7, 9])
Thay thế phần tử thứ 3 đến thứ 5 là 4,6,8. (Kết quả: a = [0, 1, 4, 6, 8, 9])
'''
def thay_doi_list(list):
    a[0]=0
    a[2]=4
    a[3]=6
    a[5]=8
    return a

if __name__ == "__main__":
    a=[1, 1, 2, 5, 7, 9]
    thay_doi_list(list)
    print(f"chuoi sau khi thay the : {a}")
