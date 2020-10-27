import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

try:
	conn = pymysql.connect(host='localhost', database='roytuts', user='root', password='root')
	cur = conn.cursor()
	_hashed_password = generate_password_hash('secret')
	cur.callproc('sp_createUser',('Soumitra Roy','contact@roytuts.com',_hashed_password))
	data = cur.fetchall()
	if len(data) == 0:
		conn.commit()
		print('User information saved successfully !')
	else:
		print('error: ', str(data[0]))
except Exception as e:
	print(e)
finally:
	cur.close() 
	conn.close()