# Usando a imagem base do Python
FROM python:3.9-slim

# Configurando o diretório de trabalho
WORKDIR /app

# Copiando os arquivos necessários para o contêiner
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definindo a porta que será exposta
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
