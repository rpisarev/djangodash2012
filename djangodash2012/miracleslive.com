upstream djangodash_server{
    server unix:/tmp/djangodash2012.sock fail_timeout=0;
}

server {
    listen 80;
    server_name miracleslive.com;
    proxy_connect_timeout 300s;
    proxy_read_timeout 300s;

    location / {
	auth_basic "Miracle Dev";
	auth_basic_user_file /root/www/androidlib/.htpasswd;
        client_max_body_size 20m;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://djangodash_server;

    }

    

    location /media {
        alias /root/www/djangodash2012/djangodash2012/media;
    }

    location /static {
        alias /root/www/djangodash2012/djangodash2012/static;
    }
    

    access_log /var/log/nginx/djangodash2012.access.log;
    error_log /var/log/nginx/djangodash2012.error.log;

}

