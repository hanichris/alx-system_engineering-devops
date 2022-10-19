#Using `Puppet`resource `file_line` to make changes to a configuration file
file_line { 'Define the Identity file to use':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Disable password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

include stdlib
