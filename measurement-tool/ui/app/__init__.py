"""Lecta değerlendirme arayüzü (TASARIM.md). Flask + Jinja + htmx; veritabanı yok.

Ortam değişkenleri:
  LECTA_DATA              değerlendirme dizinlerinin kökü (zorunlu; lecta-framework dışında)
  LECTA_USER              yerel geliştirmede kullanıcı kimliği; tanımlıysa başlığa bakılmaz
  LECTA_TRUSTED_PROXIES   X-Remote-User başlığına güvenilen adresler, virgülle (varsayılan 127.0.0.1)
  LECTA_FRAMEWORK_COMMIT  imajın build edildiği framework commit'i (ekranın altında gösterilir)
  LECTA_KULLANICILAR      arayüz kullanıcıları, virgülle (gözden geçiren seçimi; htpasswd ile aynı adlar)
"""
import os

from flask import Flask, abort, g, request

from . import framework, rotalar
from .depo import Depo


def create_app(ayar=None):
    app = Flask(__name__)
    app.config.update(
        LECTA_DATA=os.environ.get('LECTA_DATA'),
        LECTA_USER=os.environ.get('LECTA_USER', '').strip(),
        LECTA_TRUSTED_PROXIES=os.environ.get('LECTA_TRUSTED_PROXIES', '127.0.0.1'),
        LECTA_FRAMEWORK_COMMIT=os.environ.get('LECTA_FRAMEWORK_COMMIT', 'dev'),
        LECTA_KULLANICILAR=os.environ.get('LECTA_KULLANICILAR', ''),
        MAX_CONTENT_LENGTH=1024 * 1024,
    )
    app.config.update(ayar or {})
    if not app.config['LECTA_DATA']:
        raise RuntimeError('LECTA_DATA tanımlı değil')
    os.makedirs(app.config['LECTA_DATA'], exist_ok=True)
    app.extensions['depo'] = Depo(app.config['LECTA_DATA'])
    guvenilen = {x.strip() for x in app.config['LECTA_TRUSTED_PROXIES'].split(',') if x.strip()}

    @app.before_request
    def kimlik():
        if request.endpoint in ('saglik', 'static'):
            return
        # Yerelde LECTA_USER; sunucuda Apache'nin doğruladığı kullanıcı, yalnız güvenilen vekilden (§5.3)
        k = app.config['LECTA_USER']
        if not k and request.remote_addr in guvenilen:
            k = request.headers.get('X-Remote-User', '').strip()
        if not k:
            abort(401)
        g.kullanici = k

    @app.context_processor
    def ortak():
        return dict(kullanici=g.get('kullanici'), commit=app.config['LECTA_FRAMEWORK_COMMIT'],
                    surum=framework.surum())

    @app.before_request
    def baska_siteden_yazma_yok():
        # Basic auth kimliği tarayıcıda saklanır; başka bir siteden gönderilen form onu taşıyabilir (CSRF)
        if request.method == 'POST' and request.headers.get('Sec-Fetch-Site', 'same-origin') not in ('same-origin', 'none'):
            abort(403)

    @app.get('/saglik')
    def saglik():
        return 'ok'

    app.register_blueprint(rotalar.bp)
    return app
