
import pymysql

conn_obj = pymysql.connect(
    host="localhost",
    user="root",
    password="WELCOMe@1234",
    database="login_logout")
cur_obj = conn_obj.cursor()


#Define function data_entry_sql
def data_entry_sql(user_name, user_address, user_ph, user_id, user_password):
    # Build the query with user-provided name using LIKE operator
    sql = ("INSERT INTO cust_details (cust_name, cust_add, cust_ph, cust_userid, cust_password) VALUES (%s, %s, "
           "%s, %s,%s)")
    data = (user_name, user_address, user_ph, user_id, user_password)

    try:
        cur_obj.execute(sql, data)
        print(sql)
        #print("NEW CUSTOMER ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


#Define function data_retrieve
def data_retrieve(user_id):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    global result
    query = "select * from cust_details WHERE cust_userid=\'{}\'".format(user_id)#\"{user_id}\""
    #query = f"select * from cust_details WHERE cust_userid={\'user_id\'}"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result


def phone_data_retrieve(user_ph):
    #Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    global result
    query = "select * from cust_details WHERE cust_ph={}".format(user_ph)#\"{user_ph}\""

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result


def login_entry_sql(user_id, user_name, logout_timestamp=None):
    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO audit_table (cust_name,cust_id,logout_timestamp) VALUES (%s, %s, %s)"
    data = (user_id, user_name, logout_timestamp)

    try:
        cur_obj.execute(sql, data)
        #print("NEW CUSTOMER ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


def logout_entry_sql(user_id, user_name, login_timestamp=None):
    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO audit_table (cust_name,cust_id,login_timestamp) VALUES (%s, %s, %s)"
    data = (user_id, user_name, login_timestamp)

    try:
        cur_obj.execute(sql, data)
        #print("NEW CUSTOMER ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


def password_check(data_from_sql):
    user_password = input("Enter password")
    if user_password == data_from_sql[-1]:
        return 1
    else:
        return 0


def new_registration(user_id):
    user_name = input("Enter full name : ")
    user_address = input("Enter full address : ")
    user_ph = input("Enter contact no : ")

    phone_validity = phone_check(user_ph)

    if phone_validity == 0:
        user_password = input("Enter password : ")
        data_entry_sql(user_name, user_address, user_ph, user_id, user_password)

    else:
        print("Mobile number already exists")



def phone_check(user_ph):

    phone = phone_data_retrieve(user_ph)

    if phone is None:
        return 0
    elif phone[-3] == user_ph:
        #print("Mobile number already exists")
        return 1
    
    if phone is None:
        #print("not exists")
        return 0
    elif phone[-3] == user_ph:
        #print("Mobile number already exists")
        return 1
  


user_id = input("Please enter username")
data_from_sql = data_retrieve(user_id)
#print(data_from_sql)
if data_from_sql:
    value = password_check(data_from_sql)
    if value == 1:
        login_entry_sql(data_from_sql[1], data_from_sql[-2])
        print("Access granted")
        logout_choice = input("Do you want to logout ? enter y/n")
        if logout_choice == "Y" or logout_choice == "y":
            logout_entry_sql(data_from_sql[1], data_from_sql[-2])
    else:
        print("access not granted")

else:
    new_registration(user_id)

conn_obj.close()
