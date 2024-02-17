-- setting up a database as stated in task #3
creat database if not exists hbnb_dev_db;
creat user if not exists "hbnb_dev"@"localhost" identified by "hbnb_dev_pwd";
grant all privileges on hbnb_dev_db to "hbnb_dev"@"localhost";
grant select on performance_schema to "hbnb_dev"@"localhost";
