from lxml import etree

# Đọc file XML (hoặc bạn có thể dùng etree.fromstring cho chuỗi XML)
tree = etree.parse("sv.xml")  

# 1. Lấy tất cả sinh viên
print("\n1. Lấy tất cả sinh viên:")
students = tree.xpath("/school/student")
for student in students:
    print(f"   - {etree.tostring(student, encoding='unicode', pretty_print=True).strip()}")

print("\n1. Lấy tất cả sinh viên:")
students = tree.xpath("/school/student")
for student in students:
    name = student.xpath("name/text()")[0]
    date = student.xpath("date/text()")[0]
    print(f"   - {name} ({date} tuổi)")

# 2. Liệt kê tên tất cả sinh viên
print("\n2. Liệt kê tên tất cả sinh viên:")
names = tree.xpath("/school/student/name/text()")
for name in names:
    print(f"   - {name}")

# 3. Lấy tất cả id của sinh viên
print("\n3. Lấy tất cả id của sinh viên:")
ids = tree.xpath("/school/student/id/text()")
for id_val in ids:
    print(f"   - {id_val}")

# 4. Lấy ngày sinh của sinh viên có id = "SV01"
print("\n4. Lấy ngày sinh của sinh viên có id = 'SV01':")
date = tree.xpath("/school/student[id='SV01']/date/text()")
print(f"   - {date[0] if date else 'Không tìm thấy'}")

# 5. Lấy các khóa học
print("\n5. Lấy các khóa học:")
courses = tree.xpath("/school/enrollment/course/text()")
for course in courses:
    print(f"   - {course}")

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
print("\n6. Lấy toàn bộ thông tin của sinh viên đầu tiên:")
first_student = tree.xpath("/school/student[1]/*")
if first_student:
    print(f"   {etree.tostring(first_student[0], encoding='unicode', pretty_print=True).strip()}")

# 7. Lấy mã sinh viên đăng ký khóa học "Vatly203"
print("\n7. Lấy mã sinh viên đăng ký khóa học 'Vatly203':")
student_refs = tree.xpath("/school/enrollment[course='Vatly203']/studentRef/text()")
for ref in student_refs:
    print(f"   - {ref}")

# 8. Lấy tên sinh viên học môn "Toan101"
print("\n8. Lấy tên sinh viên học môn 'Toan101':")
names = tree.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()")
for name in names:
    print(f"   - {name}")

# 9. Lấy tên sinh viên học môn "Vatly203"
print("\n9. Lấy tên sinh viên học môn 'Vatly203':")
names = tree.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()")
for name in names:
    print(f"   - {name}")

# 10. Lấy ngày sinh của sinh viên có id="SV01"
print("\n10. Lấy ngày sinh của sinh viên có id='SV01':")
date = tree.xpath("/school/student[id='SV01']/date/text()")
print(f"   - {date[0] if date else 'Không tìm thấy'}")

# 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
print("\n11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997:")
students_1997 = tree.xpath("/school/student[starts-with(date, '1997')]")
for student in students_1997:
    name = student.xpath("name/text()")[0]
    date = student.xpath("date/text()")[0]
    print(f"   - Tên: {name}, Ngày sinh: {date}")

# 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
print("\n12. Lấy tên của các sinh viên có ngày sinh trước năm 1998:")
names = tree.xpath("/school/student[substring(date, 1, 4) < '1998']/name/text()")
for name in names:
    print(f"   - {name}")

# 13. Đếm tổng số sinh viên
print("\n13. Đếm tổng số sinh viên:")
count = tree.xpath("count(/school/student)")
print(f"   - Tổng số: {int(count)}")

# 14. Lấy sinh viên chưa đăng ký môn nào
print("\n14. Lấy sinh viên chưa đăng ký môn nào:")
unregistered = tree.xpath("/school/student[not(id = /school/enrollment/studentRef)]")
for student in unregistered:
    id_val = student.xpath("id/text()")[0]
    name = student.xpath("name/text()")[0]
    print(f"   - {id_val}: {name}")

# 15. Lấy phần tử <date> anh em ngay sau <name> của SV01
print("\n15. Lấy phần tử <date> anh em ngay sau <name> của SV01:")
date = tree.xpath("/school/student[id='SV01']/name/following-sibling::date[1]/text()")
print(f"   - {date[0] if date else 'Không tìm thấy'}")

# 16. Lấy phần tử <id> anh em ngay trước <name> của SV02
print("\n16. Lấy phần tử <id> anh em ngay trước <name> của SV02:")
id_val = tree.xpath("/school/student[id='SV02']/name/preceding-sibling::id[1]/text()")
print(f"   - {id_val[0] if id_val else 'Không tìm thấy'}")

# 17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'
print("\n17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03':")
courses = tree.xpath("/school/enrollment[studentRef='SV03']/course/text()")
for course in courses:
    print(f"   - {course}")

# 18. Lấy sinh viên có họ là "Trần"
print("\n18. Lấy sinh viên có họ là 'Trần':")
students = tree.xpath("/school/student[starts-with(name,'Trần')]")
for student in students:
    id_val = student.xpath("id/text()")[0]
    name = student.xpath("name/text()")[0]
    print(f"   - {id_val}: {name}")

# 19. Lấy năm sinh của sinh viên SV01
print("\n19. Lấy năm sinh của sinh viên SV01:")
year = tree.xpath("substring(/school/student[id='SV01']/date,1,4)")
print(year)