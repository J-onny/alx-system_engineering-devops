user { 'holberton':
  ensure  => present,
  shell   => '/bin/bash',
  require => Package['login'],
}

file_line { 'holberton-limits':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 8192',
  match   => '^holberton',
  ensure  => present,
  require => Package['login'],
}

exec { 'update-pam-config':
  command     => '/usr/sbin/pam-auth-update',
  refreshonly => true,
  subscribe   => File_line['holberton-limits'],
  require     => Package['login'],
}

