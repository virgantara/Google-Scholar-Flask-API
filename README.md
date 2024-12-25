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
 docker run -d -p 7000:7000 fastapi-sinta-app
```

Save Image

```bash
 docker save -o fastapi-sinta-app.tar fastapi-sinta-app
```

Load Image

```bash
 docker load < fastapi-sinta-app.tar
```

## Contoh Requst Endpoint API :

Mengambil Data Profil Sinta Unida Gontor :

- http://localhost:7000/sinta/profile/kampus

Mengambil Data Sinta Profil Dosen : /sinta/profile/dosen/{profil_id}

- http://localhost:7000/sinta/profile/dosen/5998983

Mengambil Data Sinta Profil Dosen lebih dari satu : /sinta/hindex?profile_ids={profil_id},{profil_id},{profil_id}

- http://localhost:7000/sinta/hindex/?profile_ids=5998983,6018129

  Mengambil Data Profil Google Scholar Dosen : /gs/pub/list?gs_id={user_id}

- http://localhost:7000/gs/pub/list?gs_id=56jbnvsAAAAJ
