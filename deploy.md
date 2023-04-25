git pull
docker-compose down -v
docker-compose up -d --force-recreate --always-recreate-deps --build
