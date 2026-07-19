# 🔢 Matrix Solver (Structure Check)

# 1. Matrix 1 ke dimensions liye
rows_1 = int(input("Matrix 1 ke Rows likho: "))
colum_1 = int(input("Matrix 1 ke Columns likho: "))

# 2. Matrix 2 ke dimensions liye
rows_2 = int(input("Matrix 2 ke Rows likho: "))
colum_2 = int(input("Matrix 2 ke Columns likho: "))

# 3. Yahan humne unka sahi format (order) banaya string ki tarah
matrix_1_order = f"{rows_1}x{colum_1}"
matrix_2_order = f"{rows_2}x{colum_2}"

# 4. Print karke dikhaya
print(f"""
Hi bro, here is your Matrix analysis:
Matrix 1 ka type hai = {matrix_1_order}
Matrix 2 ka type hai = {matrix_2_order}
""")

# 5. Check kiya ki kya inka multiply hona possible hai?
if colum_1 == rows_2:
    print("✅ In dono matrices ka multiplication possible hai! Ab hum iska formula laga sakte hain.")
else:
    print("❌ Oops! Matrix 1 ke columns aur Matrix 2 ke rows match nahi kar rahe. Maths ke niyam se inka multiply nahi ho sakta.")
