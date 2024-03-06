#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Simple content, to test the configuration" | sudo tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
file='/etc/nginx/sites-available/default'
line=56
text='\t}\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}'
sed -i "${line}s~.*~${text}~" $file
service nginx restart
exit 0
