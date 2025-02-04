# Use uma imagem base do Python
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    netcat-openbsd \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Configura o diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro para aproveitar cache de camadas
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Baixar e configurar wait-for-it
RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh && \
    mv wait-for-it.sh /usr/local/bin/wait-for-it  # Renomeia ao mover

# Copiar o restante do código
COPY . .

