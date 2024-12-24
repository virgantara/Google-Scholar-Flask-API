<!-- @format -->

# Sinta & Google Scholar API with FastAPI and Docker

## cara menjalankan di terminal

```bash
uvicorn main:app --reload
```

## Cara Build Image di Docker

Build Image

```bash
 docker build -t fastapi-sinta-app .
```

Run Image di Container

```bash
 docker run -d -p 8000:7000 fastapi-sinta-app
```

Save Image

```bash
 docker save -o fastapi-sinta-app.tar fastapi-sinta-app
```

Load Image

```bash
 docker load < fastapi-sinta-app.tar
```
