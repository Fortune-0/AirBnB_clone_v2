#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "Simple content, to test the configuration" | sudo tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu /data/
file='/etc/nginx/sites-available/default'
line=56
text='}\n\tlocation hbnb_static {\n\t\talias /data/web_static/current/;\n\t}'
sed -i 
service nginx restart
