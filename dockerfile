FROM python:3.11-slim

WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
