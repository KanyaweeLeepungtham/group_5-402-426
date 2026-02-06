Gauss Elimination with Partial Pivoting: การกำจัดแบบ Gauss ที่เพิ่มระบบการสลับแถว (Pivoting)

Gauss-Jordan Elimination: การกำจัดแบบGauss-Jordan เพื่อแปลงเมทริกซ์ให้อยู่ในรูป Reduced Row Echelon Form (RREF) เพื่อหาคำตอบโดยตรง

LU Decomposition: การแยกเมทริกซ์ออกเป็น Lower (L) และ Upper (U) triangular matrices พร้อมระบบ Forward/Backward substitution

Matrix Inversion (Inverse Matrix) : การหาเมทริกซ์ส่วนกลับโดยใช้ Gauss-Jordan เพื่อนำมาใช้หาคำตอบผ่านสูตร 



สมาชิกในกลุ่ม :กัญญาวีร์ (402), สุวรา (426)


# 1. การกำจัดของเกาส์ (Gauss Elimination)
  Forward Elimination:** เปลี่ยนเมทริกซ์แต่งเติม (Augmented Matrix ) ให้เป็นเมทริกซ์สามเหลี่ยมบน (Upper Triangular Matrix)
  ใช้ **Partial Pivoting** โดยการหาค่าที่มากที่สุดในแถวที่เหลืออยู่ด้านล่าง แล้วสลับแถวนั้นขึ้นมาเป็น Pivot เพื่อลดความคลาดเคลื่อน
  ใช้ Row Operation เพื่อทำให้ค่าด้านล่าง Pivot กลายเป็น 0 ทั้งหมด
#2. Back Substitution: เริ่มหาค่าตัวแปรจากแถวล่างสุดแล้วแทนค่ากลับขึ้นไปด้านบนเพื่อหาตัวแปรที่เหลือ

# 2. การกำจัดของเกาส์-จอร์แดน (Gauss-Jordan Elimination)
   Normalization: ในแต่ละแถว หารทั้งแถวด้วยค่า Pivot เพื่อให้ตำแหน่ง Pivot มีค่าเป็น 1
   Elimination: ใช้ Row Operation กำจัดตัวเลขทั้ง ด้านบน และ ด้านล่าง ของ Pivot ให้กลายเป็น 0
   Direct Solution: เมื่อจบกระบวนการ คอลัมน์สุดท้ายของเมทริกซ์แต่งเติมจะเป็นคำตอบทันที โดยไม่ต้องแทนค่ากลับ
  
# 3. การแยกแยะเมทริกซ์ (LU Decomposition)

  Decomposition: คำนวณหาค่าในเมทริกซ์ 
  Forward Substitution: แก้สมการ  เพื่อหาเวกเตอร์ตัวแปรช่วย 
  Back Substitution: แก้สมการ  เพื่อหาคำตอบสุดท้าย 

# 4. การหาเมทริกซ์ส่วนกลับ (Matrix Inversion)

ใช้วิธีการของ Gauss-Jordan ในการหา :

1. สร้างเมทริกซ์แต่งเติม  โดย  คือ Identity Matrix
2. ทำ Gauss-Jordan Elimination กับเมทริกซ์ด้านซ้ายจนกลายเป็นเมทริกซ์เอกลักษณ์
3. เมทริกซ์ด้านขวาที่ถูกแปลงตามไปด้วยจะกลายเป็น 
4. หาคำตอบสุดท้ายจาก  ผ่านฟังก์ชัน `mat_vec_mul`
