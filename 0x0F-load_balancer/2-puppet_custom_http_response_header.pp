# HTTP header response, name X-Served-By, value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

package {'nginx':
  ensure => present,
  name   => 'nginx',
}

file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${HOSTNAME};",
  match  => '^\tlocation / {',
}

exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
