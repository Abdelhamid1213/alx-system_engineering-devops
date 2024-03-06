# Check for incorrect extension before modification
file { '/var/www/html/wp-settings.php':
  ensure => present,
  require => Exec['VerifyExtension'],
}

exec { 'VerifyExtension':
  command => 'grep -q ".phpp" /var/www/html/wp-settings.php',
  unless => 'test $? == 0', # Only run if incorrect extension is found
  provider => shell,
}

exec { 'FixWordpressSite':
  command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
  require => Exec['VerifyExtension'],
}
