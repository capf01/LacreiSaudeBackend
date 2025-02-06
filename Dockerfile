# Usa a imagem oficial do Python 3.11 na versão "slim", que é mais leve e ideal para ambientes de produção.
FROM python:3.11-slim

# Atualiza os pacotes do sistema e instala dependências essenciais para rodar a aplicação:
# - curl: Utilizado para baixar scripts e recursos externos.
# - netcat-openbsd: Ferramenta para testar conexões de rede (usada, por exemplo, no wait-for-it).
# - libpq-dev: Bibliotecas necessárias para a conexão com o PostgreSQL.
# - gcc e python3-dev: Ferramentas necessárias para compilar dependências que possuam código nativo.
# Após a instalação, remove os arquivos de cache para reduzir o tamanho da imagem.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    netcat-openbsd \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container.
# Todos os comandos subsequentes serão executados a partir deste diretório (/app).
WORKDIR /app

# Copia o arquivo requirements.txt para o container.
# Este arquivo contém a lista de dependências do projeto que serão instaladas.
COPY requirements.txt .

# Atualiza o pip para a versão mais recente e instala as dependências do projeto conforme listadas no requirements.txt.
# O uso da flag --no-cache-dir ajuda a reduzir o tamanho da imagem final.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Baixa o script "wait-for-it.sh", que será utilizado para aguardar a inicialização de serviços dependentes,
# como o banco de dados, antes de iniciar a aplicação.
# Após o download, o script recebe permissão de execução e é movido para o diretório /usr/local/bin para facilitar seu uso.
RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh && \
    mv wait-for-it.sh /usr/local/bin/wait-for-it

# Copia todo o conteúdo do diretório atual (do host) para o diretório /app dentro do container.
# Isso garante que o código-fonte do projeto esteja disponível para a aplicação.
COPY . .
