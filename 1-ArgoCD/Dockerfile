# Stage 1: Build dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Install dependencies into a local directory
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production Image
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user for security compliance
RUN useradd -m devopsuser && chown -R devopsuser /app

# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /home/devopsuser/.local
COPY . .

# Ensure the local bin is on the PATH for uvicorn
ENV PATH=/home/devopsuser/.local/bin:$PATH

# Switch to the secure user
USER devopsuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
