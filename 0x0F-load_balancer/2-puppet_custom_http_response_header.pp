# Add custom HTTP header with Puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
}

file_line { 'add custom header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "    add_header X-Served-By ${hostname};",
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
