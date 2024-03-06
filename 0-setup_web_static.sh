#!/usr/bin/env bash
# Install Nginx, make required directories, alter permissions
# display fake page for illustration, restart Nginx after edits
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>Document</title>
</head>
<body>
    <h1>This is a fake page, this is for testing only</h1>
    <p>this is also a fake p</p>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
</body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu /data/
new_server_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	add_header X-Served-By $HOSTNAME;

	location /hbnb_static {
		 alias /data/web_static/current/;
		 index index.html index.htm index.nginx-debian.html;
	}
	if (\$request_filename ~ redirect_me)
	{
		rewrite ^ https://www.youtube.com/watch?v=VZrDxD0Za9I permanent;
	}
	error_page 404 /404.html;
}"
bash -c "echo -e '$new_server_config' > /etc/nginx/sites-enabled/default"
serivce nginx restart
