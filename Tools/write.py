import os
import subprocess
import sys
import glob

# =================================================================
# Cấu hình đường dẫn
# =================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.join(BASE_DIR, '..', 'Main')
INPUT_BASE_DIR = os.path.join(BASE_DIR, '..', 'Input')
OUTPUT_BASE_DIR = os.path.join(BASE_DIR, '..', 'Output')
DATA_DIR = os.path.join(BASE_DIR, '..', 'Data') # Giả định folder Data nằm cùng cấp

def write_outputs(problem_name):
    """
    Thực hiện đọc input, chạy solution của user, và ghi output.
    
    Args:
        problem_name (str): Tên bài toán (ví dụ: Tips3, Flight_year).
    """
    
    # 1. Xác định đường dẫn cụ thể
    script_file_name = f"{problem_name}.py"
    main_path = os.path.join(MAIN_DIR, script_file_name)
    input_dir = os.path.join(INPUT_BASE_DIR, problem_name)
    output_dir = os.path.join(OUTPUT_BASE_DIR, problem_name)
    
    print(f"\n🚀 Bắt đầu xử lý bài toán: {problem_name}")
    
    # 2. Kiểm tra các điều kiện cần thiết
    if not os.path.exists(main_path):
        # Thử tìm kiếm linh hoạt (ví dụ: Tips3 -> tips3.py)
        main_path_lower = os.path.join(MAIN_DIR, f"{problem_name.lower()}.py")
        if os.path.exists(main_path_lower):
            main_path = main_path_lower
        else:
            print(f"❌ Lỗi: Không tìm thấy file code: {script_file_name} hoặc {problem_name.lower()}.py")
            return
            
    if not os.path.exists(input_dir):
        print(f"❌ Lỗi: Không tìm thấy thư mục Input cho bài: {input_dir}")
        return

    # 3. Chuẩn bị thư mục output
    os.makedirs(output_dir, exist_ok=True)
    
    # 4. Lấy danh sách các file input (.in)
    input_files = sorted(glob.glob(os.path.join(input_dir, "*.in")))
    
    if not input_files:
        print(f"⚠️ Không tìm thấy file input (.in) nào trong {input_dir}")
        return

    print(f"✅ Tìm thấy {len(input_files)} test case. Đang chạy...")
    
    # 5. Xử lý từng test case
    for inp_f in input_files:
        # Xác định tên file output tương ứng (ví dụ: 1.in -> 1.out)
        base_name = os.path.basename(inp_f)
        test_name = os.path.splitext(base_name)[0]
        out_f = os.path.join(output_dir, f"{test_name}.out")

        # Đọc input
        with open(inp_f, 'r', encoding='utf-8') as f:
            input_data = f.read()

        try:
            # Thực thi solution của user
            process = subprocess.run(
                [sys.executable, main_path],
                input=input_data,
                capture_output=True,
                text=True,
                # Giữ CWD là BASE_DIR (thư mục Tools) để script có thể đọc Data/
                cwd=BASE_DIR 
            )

            # Xử lý kết quả đầu ra
            if process.returncode != 0:
                print(f"   ❌ Test {test_name}: Lỗi Runtime!")
                output_content = f"RUNTIME ERROR:\n{process.stderr.strip()}"
            else:
                # Lấy output chuẩn (loại bỏ khoảng trắng thừa ở đầu/cuối file)
                output_content = process.stdout.strip()
                print(f"   ✅ Test {test_name}: Hoàn thành.")

            # Ghi output vào file .out
            with open(out_f, 'w', encoding='utf-8') as f_out:
                f_out.write(output_content)

        except Exception as e:
            print(f"   ❌ Test {test_name}: Lỗi Hệ thống khi chạy: {str(e)}")
            continue

    print(f"\n🎉 Quá trình ghi output cho bài {problem_name} hoàn tất.")
    print(f"Output đã được ghi vào thư mục: {output_dir}")
    print("-" * 30)

if __name__ == "__main__":
    # Lấy tên bài toán từ tham số dòng lệnh
    if len(sys.argv) < 2:
        print("Sử dụng lệnh: python write.py <Tên Bài>")
        print("Ví dụ: python write.py Tips3")
        sys.exit(1)
        
    problem_name_arg = sys.argv[1]
    write_outputs(problem_name_arg)