
#Database connection details
import pymysql

conn_obj = pymysql.connect(
    host="localhost",
    user="root",
    password="WELCOMe@1234",
    database="login_logout")
cur_obj = conn_obj.cursor()


#Define function data_entry_sql
def data_entry_sql(user_name, user_address, user_phone, user_id, user_password):
    # Build the query with user-provided name using LIKE operator
    sql = ("INSERT INTO cust_details (cust_name, cust_add, cust_ph, cust_userid, cust_password) "
           "VALUES (%s, %s, %s, %s,%s)")
    data = (user_name, user_address, user_phone, user_id, user_password)

    try:
        cur_obj.execute(sql, data)
        print("Customer entry successful")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error entering data into MySQL:", e)
        conn_obj.rollback()



#Define function data_retrieve
def data_retrieve(user_id):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    query = f"select * from cust_details WHERE cust_userid=\'{user_id}\'"
    print(query)
    try:
        cur_obj.execute(query)  # result after executing the query is stored in cur_obj
        result = cur_obj.fetchone()  # fetch one row after executing the query and store in result variable
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result
    # Print or process the retrieved data using list unpacking


def new_cust_registration(user_id):
    user_name = input("Enter your full name : ")
    user_address = input("Enter your address : ")
    user_phone = input("Enter your phone number : ")
    user_password = input("set your password : ")
    data_entry_sql(user_name, user_address, user_phone, user_id, user_password)


def login_check(details_from_database):
    user_password = input("enter your password : ")
    if user_password == details_from_database[-1]:
        print("Access granted")
    else:
        print("Access denied")


user_id = input("Please enter your username - ")
details_from_database = data_retrieve(user_id)
print(details_from_database)

if details_from_database:
    login_check(details_from_database)

else:
    new_cust_registration(user_id)
conn_obj.close()
