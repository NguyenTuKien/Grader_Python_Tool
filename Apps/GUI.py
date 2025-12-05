import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Thiết lập cửa sổ chính
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 400)
        self.setFixedSize(300, 400)
        
        # Layout chính
        main_layout = QVBoxLayout()
        
        # Màn hình hiển thị
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont('Arial', 16))
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                color: white;
                border: 2px solid #555;
                border-radius: 5px;
                padding: 10px;
                font-size: 18px;
            }
        """)
        self.display.setText('0')
        main_layout.addWidget(self.display)
        
        # Grid layout cho các nút
        grid_layout = QGridLayout()
        
        # Định nghĩa các nút
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        # Tạo các nút và thêm vào grid
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '':
                    continue
                    
                button = QPushButton(button_text)
                button.setFont(QFont('Arial', 14))
                button.setMinimumHeight(60)
                
                # Thiết lập style cho các loại nút khác nhau
                if button_text in ['C', '±', '%']:
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #a6a6a6;
                            color: black;
                            border: none;
                            border-radius: 30px;
                            font-weight: bold;
                        }
                        QPushButton:pressed {
                            background-color: #888;
                        }
                    """)
                elif button_text in ['÷', '×', '-', '+', '=']:
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #ff9500;
                            color: white;
                            border: none;
                            border-radius: 30px;
                            font-weight: bold;
                        }
                        QPushButton:pressed {
                            background-color: #cc7700;
                        }
                    """)
                else:
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #333;
                            color: white;
                            border: none;
                            border-radius: 30px;
                            font-weight: bold;
                        }
                        QPushButton:pressed {
                            background-color: #555;
                        }
                    """)
                
                # Kết nối sự kiện click
                button.clicked.connect(lambda checked, text=button_text: self.button_clicked(text))
                
                # Thêm nút vào grid (nút 0 chiếm 2 cột)
                if button_text == '0':
                    grid_layout.addWidget(button, i, j, 1, 2)
                else:
                    grid_layout.addWidget(button, i, j)
        
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
        
        # Thiết lập style cho cửa sổ
        self.setStyleSheet("background-color: black;")
        
        # Biến để lưu trạng thái
        self.reset_display = False
        self.current_operation = None
        self.operand = None
        
    def button_clicked(self, text):
        current_text = self.display.text()
        
        if text == 'C':
            self.display.setText('0')
            self.reset_display = False
            self.current_operation = None
            self.operand = None
            
        elif text == '±':
            if current_text != '0':
                if current_text.startswith('-'):
                    self.display.setText(current_text[1:])
                else:
                    self.display.setText('-' + current_text)
                    
        elif text == '%':
            try:
                value = float(current_text) / 100
                self.display.setText(str(value))
            except:
                self.display.setText('Error')
                
        elif text in ['÷', '×', '-', '+']:
            try:
                self.operand = float(current_text)
                self.current_operation = text
                self.reset_display = True
            except:
                self.display.setText('Error')
                
        elif text == '=':
            if self.current_operation and self.operand is not None:
                try:
                    current_value = float(current_text)
                    
                    if self.current_operation == '+':
                        result = self.operand + current_value
                    elif self.current_operation == '-':
                        result = self.operand - current_value
                    elif self.current_operation == '×':
                        result = self.operand * current_value
                    elif self.current_operation == '÷':
                        if current_value != 0:
                            result = self.operand / current_value
                        else:
                            self.display.setText('Error')
                            return
                    
                    # Hiển thị kết quả
                    if result.is_integer():
                        self.display.setText(str(int(result)))
                    else:
                        self.display.setText(str(result))
                        
                    self.reset_display = True
                    self.current_operation = None
                    self.operand = None
                    
                except:
                    self.display.setText('Error')
                    
        elif text == '.':
            if '.' not in current_text:
                if self.reset_display:
                    self.display.setText('0.')
                    self.reset_display = False
                else:
                    self.display.setText(current_text + '.')
                    
        else:  # Số
            if self.reset_display or current_text == '0':
                self.display.setText(text)
                self.reset_display = False
            else:
                self.display.setText(current_text + text)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()