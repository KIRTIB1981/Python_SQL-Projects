use login_logout;
CREATE TABLE cust_details (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(255) NOT NULL,
    cust_add VARCHAR(255) NOT NULL,
    cust_ph VARCHAR(10) NOT NULL,
    cust_userid VARCHAR(50) NOT NULL,
    cust_password VARCHAR(100) NOT NULL
)auto_increment=1;
drop table cust_details;
select * from cust_details;
INSERT INTO cust_details (cust_name, cust_add, cust_ph, cust_userid, cust_password)
VALUES ('John Doe', '1234 Elm Street, Springfield, IL', 877217477, 'johndoe', 'securepassword123');
INSERT INTO cust_details (cust_name, cust_add, cust_ph, cust_userid, cust_password)
VALUES ('John Doe', '1234 Elm Street, Springfield, IL', 877217477, 'johndoe', 'securepassword123');
truncate cust_details;


CREATE TABLE audit_table (
    sl_no INT AUTO_INCREMENT PRIMARY KEY,
    cust_id VARCHAR(60) NOT NULL,
    cust_name VARCHAR(255) NOT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)AUTO_INCREMENT=1;
alter table audit_table add column logout_timestamp timestamp default current_timestamp ;
alter table audit_table rename column login_time to login_timestamp;
drop table audit_table;
select * from audit_table;
INSERT INTO audit_table (cust_id, cust_name)
VALUES (101, 'John Doe');
truncate audit_table;
