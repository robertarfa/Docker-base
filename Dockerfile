FROM python:3.13.0

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#non-root user
RUN useradd -ms /bin/bash my-user
#define o usuário como padrão da imagem/container
USER my-user
CMD ["tail", "-f", "/dev/null"]

##Criando a imagem do docker##
#docker build -t docker-python .

##Criando container##
#docker run docker-python

##Criando container## + Publishing ports
#docker run -d -p 4000:4000 docker-python

# para criar um volume - pwd pegar a pasta atual e sincronizar arquivos
#docker run -v $(pwd):/app docker-python => no git bash

#docker compose up
#docker exec -it 2f6 bash
#na primeira vez pip install pipenv

#rm para remover