# Guia Rápido para Rodar Projeto Django com Docker e Docker Compose

## 📚 Sumário

- Por que usar Docker?
- Requisitos
- Passo a passo para configurar o ambiente
- Rodando o projeto Django com Docker
- Rodando o projeto com Docker Compose

---

## 🚀 Por que usar Docker?

Docker permite empacotar sua aplicação com todas as suas dependências em um **container**, garantindo que ela funcione de forma consistente em qualquer ambiente sem precisar instalar dependencias externas em seu computador como:
python
banco de dados
bibliotecas
etc.

---

## ✅ Requisitos

Antes de começar, você precisa instalar os seguintes softwares:

### 1. Docker

- Acesse: https://www.docker.com/products/docker-desktop
- Compatível com Windows, MacOS e Linux
- Após a instalação, verifique a versão:
```
docker --version
```
### 2. Docker Compose

Já vem incluso no Docker Desktop (Windows/Mac)

Para Linux, instale com:

```
sudo apt install docker-compose
```

Verifique se está instalado:

```
docker-compose --version
```

### 🔨 Como Rodar o Projeto
1. Build da Imagem Docker
Execute no diretório raiz do projeto (onde está o Dockerfile):

```
docker-compose build
```

2. Inicializar o Projeto Django (somente na primeira vez)
Execute o container para ter acesso ao terminal:

```
docker-compose run web django-admin startproject meu_projeto .
```
Substitua meu_projeto pelo nome desejado.

### ▶️ Rodar o Servidor
Inicie o servidor Django com:

```
docker-compose up
```
Acesse seu projeto em: http://localhost:8000

Use docker-compose up -d para rodar em segundo plano (modo "detached").

### ⚙️ Comandos Úteis
Criar um novo app Django:

```
docker-compose exec web python manage.py startapp meu_app
```

Acessar o terminal do container:

```
docker-compose exec web bash
```

Parar e remover os containers:
```
docker-compose down
```

### ✅ Conclusão
Com isso, seu ambiente Django está pronto para desenvolvimento com Docker e Docker Compose. Utilize os comandos acima para gerenciar seu projeto de forma portátil, padronizada e segura.