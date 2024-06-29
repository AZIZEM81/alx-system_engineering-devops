# execute a command with peppet

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep -f killmenow',
}
