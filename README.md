# Backend clone of student crud by using FastAPI

#### This API  has 1 route

## 1) Student route

#### This route is reponsible for creating student, reading student, updating student and deleting student

# how to run locally
First clone this repo by using following command
````

git clone https://github.com/sajtj/student_crud.git

````
then 
````

cd student_crud

````

Then set the .env file

````
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=your_database
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
DATABASE_URL=mysql+pymysql://your_user:your_password@db:3306/your_database               # when runing the api service as a container
# DATABASE_URL=mysql+pymysql://your_user:your_password@0.0.0.0:3306/your_database        # when runing the api service locally
TEST_DATABASE_URL=mysql+pymysql://root:your_root_password@0.0.0.0:3306/your_test_database

````

Then start the services by using following command
````

docker compose up --build

````

Then you can use following link to use the  API

````

http://127.0.0.1:8000/docs 

````

Note : be careful about alembic for migrations.