import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="iti",
  database="python",
  auth_plugin='mysql_native_password'
) 
mycursor = mydb.cursor()

def get_all_employees():
    mycursor.execute("SELECT * FROM employees")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def get_employee(emp_id):
    sql = "SELECT * FROM employees WHERE id = %s"
    val = (emp_id)
    mycursor.execute(sql, (val,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def fire(emp_id):
    sql = "DELETE FROM employees WHERE id = %s"
    val = (emp_id)
    mycursor.execute(sql, (val,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def hire(employee):
    sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
    val = (employee["name"], employee["email"])
    mycursor.execute(sql,(val,))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
