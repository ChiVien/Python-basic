'''
BT4:
Giả sử có một chuỗi như sau: “0001;10:18:25;0983876207;0918295063”, tách chuỗi
trên thành từng phần riêng biệt

Cho biết vị trí thứ 2 trong chuỗi trên là thời gian cuộc gọi từ số thứ 1
“0983876207” sang số thứ 2 “0918295063”. Biết rằng 1 phút cho mỗi cuộc gọi
là 2500đ, tính giá cước cuộc gọi trên.
Gợi ý: dùng hàm input yêu cầu người dùng nhập giá trị
- Dùng hàm split để tách chuỗi

2

- Xác định vị trí thời gian cuộc gọi là vị trí thứ 2
- Chuyển đổi số trên thành kiểu số (có khả năng tính toán được)
- 2500đ 1 phút thì tính ra 1s là bao nhiều?
- Sau đó lấy 2 giá trị nhân nhau cho ra kết quả giá tiền của cuộc gọi điện thoại trên.
'''
def tinh_tien_dt(str):
    b=a.split(';')
    tg=b[1].split(':')
    tongtg=(float(tg[0])*60+float(tg[1])+round(float(tg[2])/60))
    tongtien=tongtg*2500
    return tongtien
if __name__ == "__main__":
    a=input('nhap chuoi: ')
    tinh_tien_dt(str)
    kq=tinh_tien_dt(str)
    print(f'tong tien dt: {kq}')
    