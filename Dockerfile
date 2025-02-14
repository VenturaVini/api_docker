# Usa a imagem que já contém o uv instalado
FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências usando uv
RUN pip install -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "api_completo:app", "--host", "0.0.0.0", "--port", "8000"]


