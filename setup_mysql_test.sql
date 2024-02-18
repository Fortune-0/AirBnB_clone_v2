-- Setting up a database as stated in task #4
-- Database creation
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- User creation
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
-- privileges granting
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
-- privileges granting
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
