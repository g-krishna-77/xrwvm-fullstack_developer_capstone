FROM node:16 as backend-builder
WORKDIR /app/server/database
COPY server/database/package*.json ./
RUN npm install

FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

WORKDIR $APP

# Install Node.js for backend
RUN apt-get update && apt-get install -y nodejs npm mongodb-mongosh && rm -rf /var/lib/apt/lists/*

# Copy backend
COPY --from=backend-builder /app/server/database /app/server/database
COPY server/database /app/server/database

# Install Python requirements
COPY server/requirements.txt $APP
RUN pip3 install -r requirements.txt

# Copy project
COPY server /app
COPY . $APP

EXPOSE 8000 3000

# Start both MongoDB, Node.js, and Django
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
CMD ["sh", "-c", "mongod --bind_ip 127.0.0.1 & sleep 2 && node /app/server/database/index.js & gunicorn --bind :8000 --workers 3 djangoproj.wsgi"]
