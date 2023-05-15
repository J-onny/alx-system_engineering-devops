# Fix mginx server request limit

file { '/etc/default/nginx':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('my_module/nginx_config.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/default/nginx'],
}
