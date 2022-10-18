# Using puppet to create a file in `/tmp`.
# Requirements: file path -> `/tmp/school`
#		file permission -> `0744`
#		file owner -> www-data
#		file group -> www-data
#		file contains -> `I love Puppet`

file { 'school':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
