#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "Simple content, to test the configuration" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
file='/etc/nginx/sites-available/default'
line=56
text='\t}\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}'
sudo sed -i "${line}s~.*~${text}~" $file
sudo service nginx restart
