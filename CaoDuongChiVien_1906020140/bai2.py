'''
BT2:
Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong
năm. Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
Thí dụ: Người dùng nhập vào tháng 2, in ra màn hình là mùa Xuân.
'''
def mua_trong_nam(int):
    mua=""
    if a==1 or a==2 or a==3:
        mua="mua xuan"
    elif a==4 or a==5 or a==6:
        mua="mua ha" 
    elif a==7 or a==8 or a==9:
        mua="mua thu"
    else:
        mua="mua dong"
    return mua
if __name__ == "__main__":
    a=int(input("nhap thang: "))
    while a>12:
        a=int(input("nhap lai thang: "))
    mua_trong_nam(int)
    print(mua_trong_nam(int))
