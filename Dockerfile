# Estágio 1: Build do WebAssembly (pygbag)
FROM python:3.11-slim AS builder

WORKDIR /app

# Instalar pygbag
RUN pip install --no-cache-dir pygbag

# Copiar os arquivos do projeto para o container
COPY . .

# Executar o build do pygbag para compilar em WebAssembly
RUN python -m pygbag --build .

# Sobrescrever o index.html padrão pelo nosso customizado que está salvo em web-template/
COPY web-template/index.html build/web/index.html

# Estágio 2: Servidor Nginx para rodar o jogo
FROM nginx:alpine

# Copiar a build final do estágio 1 para a pasta pública do Nginx
COPY --from=builder /app/build/web /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
