# Increase the number of open file descriptors to solve error in Nginx
# in failing to serve a large volume of requests.

exec {'ulimit increase':
  onlyif   => 'test -e /etc/default/nginx',
  command  => 'sudo sed -i "5 s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx',
  provider => shell,
  before   => Exec['restart'],
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
