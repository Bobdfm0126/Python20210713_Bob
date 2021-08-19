import sqlite3
from sqlite3 import Cursor

sql = 'create table if not exists lotto(' \
      'id integer primary key autoincrement' \
      'n1 integer, ' \
      'n2 integer, ' \
      'n3 integer, ' \
      'n4 integer, ' \
      'n5 integer, ' \
      'n6 integer' \
      ')'

conn = sqlite3.connect('lotto.db')
cursor = conn.cursor()
cursor.execute(sql)

conn.commit()
conn.close()

print('lotto 資料表建立完成')