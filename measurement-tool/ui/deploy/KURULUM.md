# donut kurulumu — lecta-frui.deepwake.tech

İlk kurulum (talimat adım 2). donut production sunucusudur: **her adım Gökhan'ın onayıyla** çalıştırılır. Mevcut vhost'lara, fail2ban'a, OpenVPN'e ve UFW'ye dokunulmaz; yalnız ekleme yapılır.

## Karar özeti

| Konu | Seçim | Neden |
|---|---|---|
| Ad | `lecta-frui.deepwake.tech` → `A 10.11.12.1` | depo.eryol.com deseni: ad yalnız VPN içinden ulaşılabilir adrese çözülür. OpenVPN `redirect-gateway` yapıyor ama sunucunun genel IP'sine giden trafik tünel dışından gider; genel IP'ye çözülen ad VPN kısıtıyla çalışmaz |
| TLS | Let's Encrypt **DNS-01** (`certbot-dns-rfc2136`) | Ad VPN adresine çözüldüğü için HTTP-01 çalışmaz (depo.eryol.com'un sertifikası bu yüzden 1 Haziran'da yenilenemeyip süresi doldu). Yalnız `_acme-challenge.lecta-frui` ayrı ve dinamik bir alt bölge; `deepwake.tech` bölgesi statik kalır, elle düzenleme alışkanlığı değişmez |
| Erişim | `Require ip 10.11.12.0/24` **ve** htpasswd (bcrypt) | ADR-001 §5.4 |
| Kimlik | Apache `X-Remote-User`'ı doğrulanan kullanıcıyla **ezer**; uygulama başlığı yalnız Docker ağ geçidinden (172.30.0.1) kabul eder | docker-proxy istekleri ağ geçidinden iletir |
| Container | `/srv/lecta-ui`, port `127.0.0.1:8090`, ağ `172.30.0.0/24`, uid 10001, `cap_drop: ALL` | uid 1000 sunucuda `vpnkul`; 3000 ve 5001 dolu |
| Veri | `/srv/lecta-ui/data`, sahibi 10001, `700` | ADR-001 §5.4; şifresiz (kabul edilmiş risk, §7) |

## 0. Dosyaları sunucuya kopyala (Mac'ten)

```
scp -r measurement-tool/ui/deploy root@donut.eryol.com:/root/lecta-ui-deploy
```

## 1. DNS (BIND)

```
cd /etc/bind
cp zones/db.deepwake.tech zones/db.deepwake.tech.bak-20261026
cp named.conf.local named.conf.local.bak-20261026
tsig-keygen -a hmac-sha256 lecta-acme > lecta-acme.key
chown root:bind lecta-acme.key && chmod 640 lecta-acme.key
install -o bind -g bind -m 644 /root/lecta-ui-deploy/bind/db._acme-challenge.lecta-frui.deepwake.tech /var/lib/bind/
cat /root/lecta-ui-deploy/bind/named.conf.local.ek >> named.conf.local
cat /root/lecta-ui-deploy/bind/db.deepwake.tech.ek >> zones/db.deepwake.tech
sed -i 's/2026083103 ; Serial/2026102601 ; Serial/' zones/db.deepwake.tech
named-checkconf \
  && named-checkzone deepwake.tech zones/db.deepwake.tech \
  && named-checkzone _acme-challenge.lecta-frui.deepwake.tech /var/lib/bind/db._acme-challenge.lecta-frui.deepwake.tech \
  && rndc reload
```

Denetim: `dig +short @127.0.0.1 lecta-frui.deepwake.tech` → `10.11.12.1`; `dig +short @1.1.1.1 NS _acme-challenge.lecta-frui.deepwake.tech` → ns1/ns2.

## 2. Sertifika

```
apt-get -s install python3-certbot-dns-rfc2136      # önce yalnız göster: certbot paketlerine dokunuyorsa dur
apt-get install -y python3-certbot-dns-rfc2136
( umask 077; printf 'dns_rfc2136_server = 127.0.0.1\ndns_rfc2136_port = 53\ndns_rfc2136_name = lecta-acme.\ndns_rfc2136_secret = %s\ndns_rfc2136_algorithm = HMAC-SHA256\n' \
    "$(awk -F'"' '/secret/{print $2}' /etc/bind/lecta-acme.key)" > /etc/letsencrypt/lecta-rfc2136.ini )
certbot certonly --non-interactive --dns-rfc2136 \
  --dns-rfc2136-credentials /etc/letsencrypt/lecta-rfc2136.ini --dns-rfc2136-propagation-seconds 10 \
  --deploy-hook "systemctl reload apache2" -d lecta-frui.deepwake.tech
certbot renew --cert-name lecta-frui.deepwake.tech --dry-run
```

## 3. Container

```
mkdir -p /srv/lecta-ui/data && chown 10001:10001 /srv/lecta-ui/data && chmod 700 /srv/lecta-ui/data
```

Mac'ten, lecta-framework kökünde: `measurement-tool/ui/deploy/gonder.sh`

Denetim (sunucuda): `curl -s 127.0.0.1:8090/saglik` → `ok`; `curl -s -o /dev/null -w '%{http_code}' 127.0.0.1:8090/` → `401`.

## 4. htpasswd (Gökhan çalıştırır; parola sorar)

```
htpasswd -c -B /etc/apache2/lecta-ui.htpasswd gokhan
chown root:www-data /etc/apache2/lecta-ui.htpasswd && chmod 640 /etc/apache2/lecta-ui.htpasswd
```

Ayhan sonra: `htpasswd -B /etc/apache2/lecta-ui.htpasswd ayhan` (`-c` olmadan).

## 5. Apache

```
install -m 644 /root/lecta-ui-deploy/apache/lecta-frui.deepwake.tech.conf /etc/apache2/sites-available/
a2ensite lecta-frui.deepwake.tech
apache2ctl configtest && systemctl reload apache2
rm -rf /root/lecta-ui-deploy
```

## 6. Kabul

- VPN içinden `https://lecta-frui.deepwake.tech` → parola sorar → sayfanın üstünde `gokhan`, altında commit.
- VPN dışından (Mac'ten, VPN kapalı): `curl -s -o /dev/null -w '%{http_code}' --resolve lecta-frui.deepwake.tech:443:138.68.148.139 https://lecta-frui.deepwake.tech/` → `403`.
- Sahte başlık: VPN içinden `curl -u gokhan -H 'X-Remote-User: baskasi' …` → sayfada yine `gokhan`.

## Geri alma

```
a2dissite lecta-frui.deepwake.tech && systemctl reload apache2
rm /etc/apache2/sites-available/lecta-frui.deepwake.tech.conf /etc/apache2/lecta-ui.htpasswd
cd /srv/lecta-ui && docker compose down --rmi all && cd / && rm -rf /srv/lecta-ui     # veri varsa önce yedekle
certbot delete --cert-name lecta-frui.deepwake.tech && rm /etc/letsencrypt/lecta-rfc2136.ini
apt-get remove -y python3-certbot-dns-rfc2136
cd /etc/bind && cp named.conf.local.bak-20261026 named.conf.local \
  && cp zones/db.deepwake.tech.bak-20261026 zones/db.deepwake.tech \
  && sed -i 's/2026083103 ; Serial/2026102602 ; Serial/' zones/db.deepwake.tech \
  && rm lecta-acme.key /var/lib/bind/db._acme-challenge.lecta-frui.deepwake.tech* \
  && named-checkconf && rndc reload
```

## Güncelleme

Yeni sürüm: lecta-framework kökünde `measurement-tool/ui/deploy/gonder.sh`. Veri dizinine dokunmaz.

## Bilinen sınır

Sunucuda yerel bir süreç `127.0.0.1:8090`'a doğrudan istek atıp `X-Remote-User` gönderebilir (istek ağ geçidinden geldiği için güvenilir sayılır). Sunucuda root dışında etkileşimli kullanıcı yoksa kabul edilebilir; ADR-001'deki "yalnız 127.0.0.1'e güven" kuralının pratikteki karşılığı budur.
