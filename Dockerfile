# Usa a imagem oficial do Jenkins LTS
FROM jenkins/jenkins:lts  

# Usuário root para instalar pacotes
USER root

# Instala Docker, Git e remove arquivos desnecessários
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    && rm -rf /var/lib/apt/lists/*

# Volta para o usuário Jenkins
USER jenkins

# Instala os plugins necessários para Pipeline e Git
RUN jenkins-plugin-cli --plugins pipeline-stage-view git

# Copia o script de configuração para o diretório correto dentro do contêiner (Esse arquivo é o que salva senha e admin)
COPY init.groovy.d /var/jenkins_home/init.groovy.d

# Expõe a porta padrão do Jenkins
EXPOSE 8080
