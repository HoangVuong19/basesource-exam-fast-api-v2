# Pull image Python 3.12.9 từ Amazon ECR
FROM public.ecr.aws/docker/library/python:3.12.9-slim

# Tao thu muc lam viec trong container
WORKDIR /app

# Copy file requirements.txt vao thu muc lam viec (neu requirements khong thay doi thi khong pip install)
COPY ./requirements.txt /app/requirements.txt

# Chay cac cau lenh build
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy toan bo source vao thu muc lam viec
COPY . .

# Chay source
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000