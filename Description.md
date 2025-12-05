
# Flight_year (Thống kê theo năm)

Dữ liệu về chuyến bay được lưu trữ trong tệp **"flights.json"** có cấu trúc từ điển lồng nhau bao gồm:

  * Ngoài cùng là từ điển có khóa là **`flights`**.
  * Giá trị của khóa danh sách các từ điển, mỗi phần tử bao gồm các khóa và giá trị text như hình:

<!-- end list -->

```json
{
  "flights": [
    {
      "year": "1949",
      "month": "January",
      "passengers": "112"
    },
    {
      "year": "1949",
      "month": "February",
      "passengers": "118"
    },
    // ...
  ]
}
```

Trong đó giá trị của khóa **`year`** là năm thống kê, giá trị của khóa **`month`** là tháng thống kê, giá trị của khóa **`passagers`** là số hành khách chở được tương ứng.

### Yêu cầu:

Đọc dữ liệu từ file JSON và in ra các thông tin thống kê theo năm.

### INPUT:

  * Dòng đầu là **số bộ Test**.
  * Các dòng tiếp theo, mỗi dòng ghi **số năm** và **chỉ số cần thống kê** (**min**, **max**, **sum**, **avg**).

### OUTPUT:

  * In ra giá trị tính được. Nếu giá trị là dạng float thì in ra **làm tròn đến 5 chữ số** sau dấu phẩy.
  * Nếu không có dữ liệu phù hợp, in ra **Invalid**.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 |  |
| 1959 sum | 5140 |
| 1950 avg | 139.66667 |

-----
# Flight 3

Dữ liệu về chuyến bay được lưu trữ trong tệp "flights.json" có cấu trúc từ điển lồng nhau bao gồm:

  - Ngoài cùng là từ điển có khóa là **flights**
  - Giá trị của khóa danh sách các từ điển, mỗi phần tử bao gồm các khóa và giá trị text như hình:

<!-- end list -->

```json
{
  "flights": [
    {
      "year": "1949",
      "month": "January",
      "passengers": "112"
    },
    {
      "year": "1949",
      "month": "February",
      "passengers": "118"
    },
    {
      "year": "1949",
      "month": "March",
      "passengers": "132"
    }
  ]
}
```

Trong đó giá trị của khóa **year** là năm thống kê, giá trị của khóa **month** là tháng thống kê, giá trị của khóa **passagers** (lưu ý: trong hình code là `passengers`) là số hành khách chở được tương ứng.

**Yêu cầu:** Đọc dữ liệu từ file JSON và in ra tổng số hành khách từ năm x đến năm thứ y.

### INPUT

Dòng đầu là số bộ Test.
Các dòng tiếp theo, mỗi dòng ghi 2 năm x và y đảm bảo x \< y.

### OUTPUT

In tổng số hành khách theo từng dòng. Nếu không có hành khách nào được chở từ năm x đến năm y in ra "Invalid".

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 |  |
| 1949 1950 | 1520 |
| 1939 1942 | Invalid |

-----
# Iris1 (Thống kê Chiều dài Đài hoa theo Loài và Cánh hoa)

Dữ liệu về hoa được lưu trữ trong tệp **`iris.csv`** có cấu trúc như sau:

```csv
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
// ...
```

Trong đó:

  * **sepal\_length:** chiều dài của đài hoa
  * **sepal\_width:** chiều rộng của đài hoa
  * **petal\_length:** chiều dài của cánh hoa
  * **petal\_width:** chiều rộng của cánh hoa
  * **species:** tên loài tương ứng (**setosa**, **virginica**, **versicolor**)

### Yêu cầu Bài toán

Viết chương trình Python đọc từ file **csv** và in ra **chiều dài trung bình của đài hoa** (`sepal_length`) khi biết tên loài (`species`) và chiều dài trung bình của cánh hoa (`petal_length`) cho trước.

### INPUT

  * Dòng đầu là **số bộ test**.
  * Các dòng tiếp theo, mỗi dòng ghi ra **tên loài** và **độ dài của cánh hoa** (`petal_length`).

### OUTPUT

  * In ra **trung bình của đài hoa** (`sepal_length`).
  * Lấy **4 chữ số thập phân sau dấu phẩy**.
  * Nếu không tìm được giá trị nào thỏa mãn yêu cầu thì in ra **Invalid**.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 | |
| setosa 1.5 | 5.15 |
| versicolor 7 | Invalid |

-----

# Penguins1 (Thống kê Kích thước Mỏ và Cánh)

File **`penguins.csv`** lưu trữ thông tin về các loài chim cánh cụt đang ở trên các đảo bao gồm các thông tin:

```csv
species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,MALE
Adelie,Torgersen,39.5,17.4,186,3800,FEMALE
Adelie,Torgersen,40.3,18,195,3250,FEMALE
// ...
```

| STT | Tên trường | Ý nghĩa | Kiểu dữ liệu |
| :---: | :--- | :--- | :--- |
| 1 | **species** | loài | chuỗi |
| 2 | **island** | đảo đang ở | chuỗi |
| 3 | **bill\_length\_mm** | độ dài cánh (mm) | số |
| 4 | **bill\_depth\_mm** | độ sâu mỏ (mm) | số |
| 5 | **flipper\_length\_mm** | flipper length (mm) | số |
| 6 | **body\_mass\_g** | trọng lượng cơ thể | số |
| 7 | **sex** | giới tính | chuỗi |

### Yêu cầu Bài toán

Viết chương trình Python đọc file và in ra **trung bình độ dài cánh** (`bill_length_mm`) và **độ sâu mỏ** (`bill_depth_mm`) theo **loài** và **đảo đang ở**.

### INPUT

  * Dòng đầu là **số n bộ test**.
  * Các dòng tiếp theo, mỗi dòng ghi một bộ test bao gồm **tên loài** và **tên đảo**.

### OUTPUT

  * Mỗi kết quả ghi trên một dòng.
  * Ghi **độ dài cánh trung bình** và **độ sâu cánh trung bình** cách nhau **1 khoảng trắng**.
  * Làm tròn đến **4 số sau dấu phẩy**.
  * Nếu không tìm thấy ghi **Invalid**.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 | |
| Adelie Torgersen | 39.1125 18.1234 |
| Adelie PhuQuoc | Invalid |

-----

# Tips1 (Thống kê theo giới tính và tình trạng hút thuốc)

Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn bao gồm các trường:

```json
{
  "tips": [
    {
      "total_bill": "16.99",
      "tip": "1.01",
      "sex": "Female",
      "smoker": "No",
      "day": "Sun",
      "time": "Dinner",
      "size": "2"
    },
    {
      "total_bill": "10.34",
      "tip": "1.66",
      "sex": "Male",
      "smoker": "No",
      // ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính (**Male** hoặc **Female**)
  * **smoker:** hút thuốc hoặc không hút (**Yes** hoặc **No**)
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn

### Yêu cầu:

Đọc từ file json và đưa ra các chỉ số thống kê (**sum**, **avg**, **max**, **min**) về tổng tiền hóa đơn (**total\_bill**) theo yêu cầu đề bài.

### INPUT:

  * Dòng đầu đưa vào số bộ test.
  * Lần lượt đưa vào giới tính và trạng thái hút thuốc.

### OUTPUT:

  * Đưa ra 1 dòng gồm các chỉ số thống kê. Các số thập phân lấy **4 chữ số** sau dấu phẩy.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 1 | |
| Male No | 1919.7500 19.7912 48.3300 7.5100 |

-----

<!-- # Tips2 (Thống kê theo giới tính và thuộc tính) 

Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn bao gồm các trường:

```json
{
  "tips": [
    {
      "total_bill": "16.99",
      "tip": "1.01",
      "sex": "Female",
      "smoker": "No",
      "day": "Sun",
      "time": "Dinner",
      "size": "2"
    },
    {
      "total_bill": "10.34",
      "tip": "1.66",
      "sex": "Male",
      "smoker": "No",
      // ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính
  * **smoker:** hút thuốc hoặc không hút
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn


### Yêu cầu

Đọc từ file **json** và đưa ra các chỉ số thống kê (**sum, avg, max, min**) về tổng tiền hóa đơn (**total\_bill**) theo yêu cầu đề bài. **Nếu giới tính hoặc thuộc tính không có trong file thì đưa ra Invalid**.

### INPUT

  * Dòng đầu đưa vào **số bộ test**.
  * Lần lượt đưa vào **giới tính** và **thuộc tính**.

### OUTPUT

  * Đưa ra **1 dòng** gồm các chỉ số thống kê.
  * Các số thập phân lấy **4 chữ số** sau dấu phẩy.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 1 |  |
| Male tip | 485.0700 3.0896 10.0000 1.0000 |
| Female tips | Invalid |

----- -->

# Tips3 (Thống kê theo ngày và số người)

Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn bao gồm các trường:

```json
{
  "tips": [
    {
      "total_bill": "16.99",
      "tip": "1.01",
      "sex": "Female",
      "smoker": "No",
      "day": "Sun",
      "time": "Dinner",
      "size": "2"
    },
    {
      "total_bill": "10.34",
      "tip": "1.66",
      "sex": "Male",
      "smoker": "No",
      // ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính
  * **smoker:** hút thuốc hoặc không hút
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn

### Yêu cầu:

Đọc từ file csv đưa ra giá trị hóa đơn trung bình (**total\_bill**) theo ngày và số người trên bàn ăn.

### INPUT:

  * Dòng đầu tiên đưa vào số bộ test.
  * Dòng thứ 2 ghi ngày và số người trên bàn ăn cách nhau **1 khoảng trắng**.

### OUTPUT:

  * Đưa ra giá trị trung bình của tổng hóa đơn (**total\_bill**). Các giá trị thập phân cách nhau bởi **1 khoảng trắng**.
  * Nếu không có dữ liệu phù hợp, in ra **Invalid**.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 | |
| Sun 2 | 17.5600 |
| Fri 10 | Invalid |

-----

# Tips4 (Thống kê theo Ngày và Buổi trong Ngày)

Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn bao gồm các trường:

```json
{
  "tips": [
    {
      "total_bill": "16.99",
      "tip": "1.01",
      "sex": "Female",
      "smoker": "No",
      "day": "Sun",
      "time": "Dinner",
      "size": "2"
    },
    {
      "total_bill": "10.34",
      "tip": "1.66",
      "sex": "Male",
      "smoker": "No",
      // ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính
  * **smoker:** hút thuốc hoặc không hút
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn

### Yêu cầu Bài toán

Đọc từ file **csv** đưa ra giá trị tiền bo trung bình (**tip**) theo **ngày (day)** và **buổi trong ngày (time)**.

### INPUT

  * Dòng đầu tiên đưa vào **số bộ test**.
  * Dòng thứ 2 ghi **ngày** và **buổi trong ngày** cách nhau **1 khoảng trắng**.

### OUTPUT

  * Đưa ra giá trị trung bình của **tổng tiền bo (tip)**, in ra 5 chữ số sau dấu phẩy.
  * Các giá trị thập phân cách nhau bởi **1 khoảng trắng**.
  * Nếu không có dữ liệu phù hợp, in ra **Invalid** (suy ra từ ví dụ).

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 | |
| Sun Dinner | 3.2551 |
| Sun Break | Invalid |

-----

# Titanic1 (Thống kê Sống Sót theo Lớp vé và Giới tính) 

Titanic là dữ liệu về vụ đắm tàu kinh hoàng năm 1912. File bao gồm thông tin những người đã tham gia chuyến tàu Titanic.

File dữ liệu **titanic.csv** có dạng:
```csv
survived,pclass,sex,age,sibsp,parch,fare,embarked,class,who,adult_male,deck,embark_town,alive,alone
1,1,male,16.5,5,1,439.5685,S,First,man,True,F,Southampton,yes,False
1,2,female,68.0,0,1,420.6682,Q,Second,woman,False,,Queenstown,yes,False
1,1,male,34.1,5,2,319.0723,C,First,man,True,,Cherbourg,yes,False
0,2,male,67.0,2,0,236.5879,C,Second,man,True,B,Cherbourg,no,False
1,1,female,66.2,1,2,50.939,C,First,woman,False,F,Cherbourg,yes,False
0,3,male,56.5,2,0,109.0144,Q,Third,man,True,,Queenstown,no,False
0,2,male,76.7,0,0,462.8162,Q,Second,man,True,A,Queenstown,no,True
0,2,male,35.4,1,2,157.7659,Q,Second,man,True,C,Queenstown,no,False
```

**Mô tả các trường:**

| STT | Tên trường | Kiểu dữ liệu | Ví dụ | Ý nghĩa |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **survived** | int | 0/1 | sống hoặc chết |
| 2 | **pclass** | int | 1/2/3 | lớp vé |
| 3 | **sex** | string | female/male | giới tính |
| 4 | **age** | float | 28.5/40.0/... | tuổi |
| 7 | **fare** | float | 7.25/53.1/... | giá vé |
| 9 | **class** | string | Third/First/... | lớp |
| 13 | **alive** | string | no/yes | còn sống không |
| 14 | **alone** | boolean | True/False | có một mình không |
| ... | *(và các trường khác)* | | | |

### Yêu cầu Bài toán

Đọc từ file **csv** và đếm số lượng người còn sống và đã chết theo **lớp vé** và **giới tính** trong vụ đắm tàu.

### INPUT
* Dòng đầu ghi **số lượng bộ test**.
* Các dòng sau, mỗi dòng ghi lần lượt **lớp vé** và **giới tính** cách nhau **1 khoảng trắng**.

### OUTPUT
* Ghi ra **số người còn sống** và **đã chết** cách nhau **1 khoảng trắng**.
* Nếu không tìm thấy ghi ra **Invalid**.

### Ví dụ:

| Input | Output |
| :--- | :--- |
| 2 | |
| 2 male | 17 91 |
| 1 kid | Invalid |