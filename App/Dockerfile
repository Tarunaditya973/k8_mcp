FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install mcp[cli] kubernetes
CMD ["python", "server.py"]