# Usa a imagem oficial do Python 3.11 na versão "slim", que é mais leve
FROM python:3.11-slim

# Atualiza os pacotes e instala dependências necessárias para rodar a aplicação
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \                 
    netcat-openbsd \        
    libpq-dev \             
    gcc \                   
    python3-dev \           
    && rm -rf /var/lib/apt/lists/*
    
# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Atualiza o pip e instala as dependências do projeto listadas no requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Baixa o script "wait-for-it.sh", que será usado para aguardar a inicialização do banco de dados
RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh && \ 
    mv wait-for-it.sh /usr/local/bin/wait-for-it  
# Copia todo o conteúdo do diretório local para dentro do container no diretório /app
COPY . .