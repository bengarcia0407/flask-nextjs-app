FROM mcr.microsoft.com/devcontainers/python:3.11

# Node.js for Next.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Upgrade pip
RUN pip install --upgrade pip
