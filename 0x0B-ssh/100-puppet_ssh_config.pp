# change ssh config file
exec { 'echo':
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
