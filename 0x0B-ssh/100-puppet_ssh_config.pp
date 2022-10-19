#Using `Puppet`resource `file_line` to make changes to a configuration file
file { '/root/.ssh/config':
  ensure  => present,
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no",
}
