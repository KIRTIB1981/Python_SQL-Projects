create database store_inventory;
use store_inventory;
set sql_safe_updates=0;
drop table store_inventory_table;
create table store_inventory_table(
product_id varchar(30) not null,
product_name varchar(100) not null,
product_price decimal(10,2) not null,
product_quantity int not null);
alter table store_inventory_table add constraint primary key(product_id);
describe store_inventory_table;

select * from store_inventory_table;
update store_inventory_table set product_quantity = 40 where product_id = '10112';
insert into store_inventory_table values('10112','toothpaste',99.99,20);