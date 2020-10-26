'''
BT3:
Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13),
nếu chạy đến số 13 thì không chạy nữa (không cộng số 13) và xuất kết quả
Ví dụ: input: n = 20
Output: S = 78
'''
def tinh_tong(int):
    S=0
    for i in range(n+1):
        if i<13:
            S+=i
        elif i==13:
            break
    return S
if __name__ == "__main__":
    n=int(input('nhap N: '))
    print(tinh_tong(int))
