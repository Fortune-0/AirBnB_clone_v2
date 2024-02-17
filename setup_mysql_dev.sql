-- Setting up a database as stated in task #3
-- Database creation
create database if not exists hbnb_dev_db;
-- User creation
create user if not exists "hbnb_dev"@"localhost" identified by "hbnb_dev_pwd";
-- privileges granting
grant all privileges on hbnb_dev_db.* to "hbnb_dev"@"localhost";
-- privileges granting
grant select on performance_schema.* to "hbnb_dev"@"localhost";
flush privileges;
