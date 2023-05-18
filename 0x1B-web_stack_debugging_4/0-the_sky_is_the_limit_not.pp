# puppet configuring numbers of requests

file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"/n',
}
