# 1-user_limit.pp
# Increases hard and soft file limits for the holberton user

# Increase hard file limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/c\holberton hard nofile 50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/c\holberton soft nofile 50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
