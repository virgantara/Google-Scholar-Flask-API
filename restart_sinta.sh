docker build -t sinta-gs-api-img .
docker stop container sinta-gs-api-img
docker rm sinta-gs-api-img
docker run -d --name sinta-gs-api -p 5000:7000 sinta-gs-api-img