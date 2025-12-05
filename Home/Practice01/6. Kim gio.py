import math

if __name__ == '__main__':
    h, m, s = map(int, input().split())
    
    # Tính góc kim giờ so với vị trí 12 giờ
    # h giờ: h * 30 độ
    # m phút: m * 0.5 độ (kim giờ di chuyển liên tục)
    # s giây: s * (0.5/60) độ = s/120 độ
    
    angle = h * 30 + m * 0.5 + s / 120
    
    print("Angle:", angle)