import sqlite3
# 建立一個 financial 財務部門

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

sql = "Update departments set dept_name'%s' where dept_id=%d" % ('Financial', 5)

conn.commit()
conn.close()

print('Update ok')

