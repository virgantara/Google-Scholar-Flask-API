# Menggunakan image Python sebagai base
FROM python:latest

# Menentukan working directory dalam container
WORKDIR /app

# Menyalin file requirements dan kode aplikasi ke dalam container
COPY requirements.txt /app/requirements.txt
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Menentukan port yang akan digunakan
EXPOSE 7000

# Menjalankan aplikasi FastAPI menggunakan Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000", "--reload"]