-- setting up a database as stated in task #3
create database if not exists hbnb_dev_db;
create user if not exists "hbnb_dev"@"localhost" identified by "hbnb_dev_pwd";
grant all privileges on hbnb_dev_db to "hbnb_dev"@"localhost";
grant select on performance_schema to "hbnb_dev"@"localhost";
