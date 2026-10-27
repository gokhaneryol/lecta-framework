# Build bağlamı: measurement-tool/ (compose.yaml bunu ayarlar)
FROM python:3.12-slim

ARG FRAMEWORK_COMMIT=dev
LABEL org.opencontainers.image.title="lecta-ui" \
      org.opencontainers.image.revision="${FRAMEWORK_COMMIT}"
ENV LECTA_FRAMEWORK_COMMIT="${FRAMEWORK_COMMIT}" \
    LECTA_DATA=/data \
    HOME=/tmp \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app/measurement-tool
# Yeni değerlendirme dizini git deposu olarak açılır (TASARIM.md §5.4)
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
COPY ui/requirements.txt ui/requirements.txt
RUN pip install --no-cache-dir -r ui/requirements.txt

COPY source source
COPY tools tools
COPY ui/app ui/app

# uid 1000 donut'ta vpnkul; çakışmasın diye ayrı uid. Sunucudaki /data dizini bu uid'e ait olur.
ARG LECTA_UID=10001
RUN useradd --uid "${LECTA_UID}" --no-create-home lecta && mkdir -p /data && chown lecta /data
USER lecta
EXPOSE 8000
# Tek worker + thread'ler (TASARIM.md §5.3); dosya kilitleri süreçler arası da çalışır
CMD ["gunicorn", "--workers", "1", "--threads", "8", "--bind", "0.0.0.0:8000", \
     "--chdir", "ui", "app:create_app()"]
