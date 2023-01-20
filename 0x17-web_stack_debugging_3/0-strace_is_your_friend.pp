# Puppet manifest to fix 500 internal server error for Apache

exec {'substitute':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
