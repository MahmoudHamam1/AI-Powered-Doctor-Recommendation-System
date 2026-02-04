from mcr.microsoft.com/devcontainers/python:3.12

# Install uv system-wide
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN mv /root/.local/bin/uv /usr/local/bin/uv
RUN pip install --upgrade pip
ENV PATH="/usr/local/bin:$PATH"
ENV DEVCONTAINER=Yes



