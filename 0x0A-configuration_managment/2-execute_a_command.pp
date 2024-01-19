# Using Puppet, create a manifest that kills a process named killmenow
# The process is terminated using the pkill command.

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
