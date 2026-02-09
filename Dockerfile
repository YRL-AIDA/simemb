FROM pytorch/pytorch:2.10.0-cuda13.0-cudnn9-runtime

COPY . /app

WORKDIR /app

RUN uv venv
RUN uv pip install .

# set HF_HOME to cache models in container (or mount volume)
ENV HF_HOME=/app/.cache/huggingface

EXPOSE 8000

CMD ["uv", "run", "python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
