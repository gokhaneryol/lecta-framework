#!/bin/sh
# Arayüzü donut'a gönderir: measurement-tool'un HEAD'ini /srv/lecta-ui/src'ye açar, imajı build eder, container'ı yeniler.
# Kullanım (lecta-framework kökünden, temiz çalışma ağacıyla): measurement-tool/ui/deploy/gonder.sh
set -eu
HOST=${LECTA_HOST:-root@donut.eryol.com}
test -z "$(git status --porcelain)" || { echo "çalışma ağacı temiz değil" >&2; exit 1; }
SHA=$(git rev-parse --short HEAD)
git archive --format=tar HEAD:measurement-tool | ssh "$HOST" '
  set -e; cd /srv/lecta-ui
  rm -rf src.yeni && mkdir src.yeni && tar -x -C src.yeni
  rm -rf src && mv src.yeni src'
scp -q measurement-tool/ui/deploy/compose.donut.yaml "$HOST:/srv/lecta-ui/compose.yaml"
ssh "$HOST" "cd /srv/lecta-ui && echo FRAMEWORK_COMMIT=$SHA > .env && docker compose up -d --build && docker compose ps"
echo "gönderildi: $SHA"
