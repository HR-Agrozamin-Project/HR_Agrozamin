# HR_Agrozamin


## django-admin makemessages -l ru
## django-admin compilemessages

ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';


server {
    listen 80;
    server_name 139.162.159.187;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /root/HR_agrozamin/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/root/HR_agrozamin/app.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/HR_Agrozamin /etc/nginx/sites-enabled