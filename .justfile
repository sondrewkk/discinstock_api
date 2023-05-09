dev:
  poetry run uvicorn --host 0.0.0.0 --port 8088 --reload app.main:app

clean:
  sudo rm -rf ./docker/data/*

start-db:
  docker stack deploy -c docker/docker-compose.yml mongodb

stop-db:
  docker stack rm mongodb