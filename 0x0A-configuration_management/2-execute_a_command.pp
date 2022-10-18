#using `Puppet` to kill a particular running process.
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
