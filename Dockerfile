# Usa a imagem base oficial do Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Exponha a porta 5000 para o host
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
