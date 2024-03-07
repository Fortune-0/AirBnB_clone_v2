# Redos task #0 but by using Puppet

exec {'updateing the packages':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['installing Nginx'],
}

exec {'installing Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['starting Nginx'],
}

exec {'starting Nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['creating directory'],
}

exec {'creating directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['creating another directory'],
}

exec {'creating another directory':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['html'],
}

exec {'html':
  provider => shell,
  command  => 'echo "Simple content, to test the configuration" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

exec {'symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['location'],
}

exec {'location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
