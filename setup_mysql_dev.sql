-- Setting up a database as stated in task #3
-- Database creation
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- User creation
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
-- privileges granting
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
-- privileges granting
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
