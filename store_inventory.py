import pymysql
import QRScanner

from warnings import filterwarnings
filterwarnings(action='ignore')


conn_obj = pymysql.connect(
    host="localhost",
    user="root",
    password="WELCOMe@1234",
    database="store_inventory")
cur_obj = conn_obj.cursor()


def add_product_to_inventory(pr_id, pr_name, pr_price, pr_quantity):
    query = (
        "insert into store_inventory_table (product_id, product_name, product_price, product_quantity) values(%s,%s,%s,"
        "%s)")
    data = (pr_id, pr_name, pr_price, pr_quantity)

    try:
        cur_obj.execute(query, data)
        print("product entry successful")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


def update_product_to_inventory(pr_id,updated_pr_quantity):
    query = (
        f"update store_inventory_table set product_quantity = %s where product_id = %s ")
    data = (updated_pr_quantity, pr_id)

    try:
        cur_obj.execute(query,data)
        print("product quantity updated successfully")
        print(query)
        conn_obj.commit()
        print(cur_obj.rowcount, "record(s) affected")
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


def retrieve_product_from_inventory(pr_id):
    query = f"select * from store_inventory_table where product_id = \'{pr_id}\'"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error in retrieving data")
        conn_obj.rollback()
    if result:
        return result
    else:
        print("product is not listed in inventory")


def add_product():
    pr_name = input("enter product name :")
    pr_id = input("enter product id :")
    pr_price = float(input("enter product price :"))
    pr_quantity = int(input("enter product quantity :"))
    add_product_to_inventory(pr_id, pr_name, pr_price, pr_quantity)


def update_product(pr_id):
    pr_present = retrieve_product_from_inventory(pr_id)
    if pr_present:
        pr_quantity = int(input("enter product quantity :"))

        updated_pr_quantity = pr_present[-1] + pr_quantity

        update_product_to_inventory(pr_id,updated_pr_quantity)
    else:
        add_product()


option = int(input("enter 1 for adding product/2 for updating product quantity"))
if option == 1:
    add_product()
elif option == 2:
    pr_id = input("enter product id :")
    update_product(pr_id)
