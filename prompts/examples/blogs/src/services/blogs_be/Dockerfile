FROM blogs_base_python

# Copy each library
COPY libs/woodstock /app/libs/woodstock

# Install the service
COPY services/blogs_be /app/src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --break-system-packages -e /app/src -r /app/src/requirements.txt

WORKDIR /app/src
