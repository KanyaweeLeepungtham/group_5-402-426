Gauss Elimination with Partial Pivoting: การกำจัดแบบ Gauss ที่เพิ่มระบบการสลับแถว (Pivoting)

Gauss-Jordan Elimination: การกำจัดแบบGauss-Jordan เพื่อแปลงเมทริกซ์ให้อยู่ในรูป Reduced Row Echelon Form (RREF) เพื่อหาคำตอบโดยตรง

LU Decomposition: การแยกเมทริกซ์ออกเป็น Lower (L) และ Upper (U) triangular matrices พร้อมระบบ Forward/Backward substitution

Matrix Inversion (Inverse Matrix) : การหาเมทริกซ์ส่วนกลับโดยใช้ Gauss-Jordan เพื่อนำมาใช้หาคำตอบผ่านสูตร 



สมาชิกในกลุ่ม :กัญญาวีร์ (402), สุวรา (426)


# 1. การกำจัดของเกาส์ (Gauss Elimination)
  •Forward Elimination: เปลี่ยนเมทริกซ์แต่งเติม (Augmented Matrix ) ให้เป็นเมทริกซ์สามเหลี่ยมล่าง
  •การหาค่าที่มากที่สุดในแถวที่เหลืออยู่ด้านล่าง แล้วสลับแถวนั้นขึ้นมาเป็น Pivot เพื่อลดความคลาดเคลื่อน
  •ใช้ Row Operation เพื่อทำให้ค่าด้านล่าง Pivot กลายเป็น 0 ทั้งหมด
#2. Back Substitution: เริ่มหาค่าตัวแปรจากแถวล่างสุดแล้วแทนค่ากลับขึ้นไปด้านบนเพื่อหาตัวแปรที่เหลือ

# 2. การกำจัดของเกาส์-จอร์แดน (Gauss-Jordan Elimination)
   Normalization: ในแต่ละแถว หารทั้งแถวด้วยค่า Pivot เพื่อให้ตำแหน่ง Pivot มีค่าเป็น 1
   Elimination: ใช้ Row Operation กำจัดตัวเลขทั้ง ด้านบน และ ด้านล่าง ของ Pivot ให้กลายเป็น 0
   Direct Solution: เมื่อจบกระบวนการ คอลัมน์สุดท้ายของเมทริกซ์แต่งเติมจะเป็นคำตอบทันที โดยไม่ต้องแทนค่ากลับ
  
# 3.LU Factorization
  1.รับเมทริกซ์ A และสร้างเมทริกซ์ L และ U ขนาดเดียวกัน โดยกำหนดค่าเริ่มต้นเป็น 0

  2.แยกเมทริกซ์ A ออกเป็น
      •    L (Lower triangular matrix)
      •    U (Upper triangular matrix)
  
  3.แก้ระบบสมการเชิงเส้น
      •    Forward Substitution : แก้ Ly = b
      •    Back Substitution : แก้ Ux = y
  
  4.ได้คำตอบสุดท้ายของระบบสมการคือ x

#Inverse Matrix (Gauss–Jordan)
  1.สร้าง Augmented Matrix
  [A \mid I]
  
  2.ทำ Gauss–Jordan Elimination
      •    เช็คว่า pivot เป็น 0 หรือใกล้ 0 (ถ้าใช่เมทริกซ์เป็น singular)
      •    ทำ pivot = 1
      •    ทำให้ตำแหน่งอื่นในคอลัมน์เป็น 0
  
  3.เมื่อด้านซ้ายเป็น Identity Matrix ด้านขวาจะเป็น A^{-1} ตอบได้เลย
  
  4.คูณ matrix กับ vector หา x โดยใช้ฟังก์ชัน mat_vec_mul
  
  5.ปัดทศนิยมเมทริกซ์ โดยฟังก์ชัน round_matrix
  
  6.ทศนิยมเวกเตอร์ โดยฟ้งก์ชัน round_vector