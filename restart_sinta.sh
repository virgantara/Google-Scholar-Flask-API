docker container stop sinta-api
docker image rm -f sinta-gs-api-img
docker build -t sinta-gs-api-img .
docker run -d --name sinta-api -p 5000:7000 sinta-gs-api-img
