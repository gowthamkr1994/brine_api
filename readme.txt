to run redis docker
docker run -p 6379:6379 redis

docker run -p 8000:8000 brine_image:latest

docker run --name mysql-latest  \
-p 3306:3306 -p 33060:33060  \
-e MYSQL_ROOT_HOST='%' -e MYSQL_ROOT_PASSWORD='root123'   \
-d mysql/mysql-server:latest