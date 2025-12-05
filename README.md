# Hướng dẫn sử dụng tools

Hệ thống chấm điểm được thiết kế để kiểm tra và đánh giá các bài tập lập trình. Dưới đây là các bước để sử dụng hệ thống:

## 1. Cấu trúc thư mục
Hệ thống yêu cầu cấu trúc thư mục như sau:
- **Description.md**: File mô tả yêu cầu và hướng dẫn cho từng bài tập.
- **Data/**: Chứa các dữ liệu cần thiết cho bài tập (ví dụ: `tips.json`, `titanic.csv`, ...).
- **Input/**: Chứa các file đầu vào cho từng bài tập.
  - Ví dụ: `Input/Tips3/1.in`, `Input/Tips3/2.in`, ...
- **Output/**: Chứa các file đầu ra mong muốn tương ứng với từng bài tập.
  - Ví dụ: `Output/Tips3/1.out`, `Output/Tips3/2.out`, ...
- **Tools/**: Chứa các công cụ hỗ trợ, bao gồm file `check.py` để chấm điểm.

## 2. Cách chạy tools
1. Đảm bảo bạn đã cài đặt Python 3 trên máy tính của mình.

2. `Clone` repository này về máy tính cá nhân:
   ```bash
   git clone <URL_REPOSITORY>
   cd <TÊN_THƯ_MỤC>
   ```

3. Viết code của bạn vào folder Home với đề bài là tên bài tập tương ứng (không phân biệt hoa thường).
    - Ví dụ: Để làm bài tập `Flight_year`, tạo file `Home/Flight_year.py` và viết code vào đó. 

4. Chạy lệnh sau để chấm điểm cho một bài tập cụ thể:
   ```bash
   python3 Tools/check.py <Tên_Bài_Tập>
   ```
   - Ví dụ: Để chấm bài tập `Tips3`, chạy lệnh:
        ```bash
        python3 Tools/check.py Tips3
        ```

5. Kết quả sẽ được hiển thị trên terminal, bao gồm số lượng test case đúng và sai.

## 3. Lưu ý
- Đảm bảo các file đầu vào và đầu ra được đặt đúng thư mục và đúng định dạng.
- Đọc kỹ file `Description.md` để hiểu yêu cầu của từng bài tập.
- Nếu có lỗi, kiểm tra lại logic trong bài làm hoặc cấu trúc thư mục.

## 4. Thông tin thêm
- Nên `fork` repository này để lưu trữ và quản lý bài làm của bạn, sau đó `clone` về máy cá nhân để làm việc.
- Nếu có lỗi, hãy mở `pull request` để đóng góp sửa lỗi cho hệ thống.
