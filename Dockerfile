FROM pytorch/pytorch:2.10.0-cuda13.0-cudnn9-runtime

COPY . /app

WORKDIR /app

RUN ls -la

RUN uv venv
RUN uv pip install .

# Optional: set HF_HOME to cache models in container (or mount volume)
ENV HF_HOME=/app/.cache/huggingface

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
