import sys

# Giữ nguyên logic check của bạn, nhưng tối ưu cú pháp
def check(s):
    # Điều kiện 1: Phải chứa đủ các số 2, 3, 5, 7
    for i in "2357":
        if i not in s:
            return False
    # Điều kiện 2: Tận cùng không được là 2 (số chẵn)
    if s[-1] == '2':
        return False
    return True

def try_gen(current_s, limit_len):
    # Nếu độ dài chuỗi hiện tại bằng độ dài mục tiêu
    if len(current_s) == limit_len:
        if check(current_s):
            print(current_s)
        return

    # Gọi đệ quy thêm dần các số 2, 3, 5, 7
    for c in "2357":
        # Tối ưu nhỏ: Nếu đang ở ký tự cuối cùng thì đừng thêm '2'
        # (để đỡ phải return False trong hàm check)
        if len(current_s) == limit_len - 1 and c == '2':
            continue
        
        try_gen(current_s + c, limit_len)

def main():
    # Đọc input nhanh
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])

    # Duyệt độ dài từ 4 đến N (để in theo thứ tự tăng dần về độ lớn)
    for length in range(4, n + 1):
        try_gen("", length)

if __name__ == "__main__":
    main()