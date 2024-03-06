# automated puppet fix (to find out why Apache is returning a 500 error)

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  replace => 'true',
  content => file('/var/www/html/wp-settings.php').content.gsub('.phpp', '.php'),
  notify  => Service['apache2'],
}
