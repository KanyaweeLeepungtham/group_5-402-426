import numpy as np
def gauss_elimination_pivoting(A, b):
    n = len(b)
    #รวมเมทริกซ์์ืั้งหมดเข้าด้วยกัน
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    for i in range(n):
        # Partial Pivoting:
        #เอาเส้นทแยงมุม
        max_row = i + np.argmax(abs(Ab[i:, i]))
        #สลับแถว
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # สร้าง Upper Triangular Matrix
        for j in range(i + 1, n):
            # ทำ roll operation
            factor = Ab[j, i] / Ab[i, i]
            # ทำ roll operation
            Ab[j, i:] -= factor * Ab[i, i:]

    # Back Substitution: หาค่า x จากล่างขึ้นบน
    x = np.zeros(n)
    # start finish backward
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    return x


def gauss_jordan_elimination(A, b):
    n = len(b)
    # รวมเมทริกทั้งหมดเข้าด้วยกัน
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    for i in range(n):
        # ทำแนวทแยงเป็น 1
        Ab[i] = Ab[i] / Ab[i, i]
        # ทำให้สมาชิกตัวอื่นเป็น 0 ทั้งหมด
        for j in range(n):
            if i != j:
                factor = Ab[j, i]
                Ab[j] -= factor * Ab[i]

    return Ab[:, -1]


# --- ทดสอบกับ Test Case จากโจทย์ ---

# ตัวอย่างที่ 1
A1 = np.array([[2, 1, 3], [4, 3, 5], [6, 5, 5]])
b1 = np.array([1, 1, -3])

# ตัวอย่างที่ 2
A2 = np.array([[2, -1, -3, 1], [1, 1, 1, -2], [3, 2, -3, -4], [-1, -4, 1, 1]])
b2 = np.array([9, 10, 6, 6])

print("--- ผลลัพธ์ตัวอย่างที่ 1 ---")
print("Gauss (Pivoting):", gauss_elimination_pivoting(A1, b1))
print("Gauss-Jordan:    ", gauss_jordan_elimination(A1, b1))

print("\n--- ผลลัพธ์ตัวอย่างที่ 2 ---")
print("Gauss (Pivoting):", gauss_elimination_pivoting(A2, b2))
print("Gauss-Jordan:    ", gauss_jordan_elimination(A2, b2))