# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up 
# your client SSH configuration file so that you can connect to a server without typing a password.
# Requirements:
# - Your SSH client configuration must be configured to use the private key ~/.ssh/school
# - Your SSH client configuration must be configured to refuse to authenticate using a password

file { '/etc/ssh/ssh_config':
  ensure => present,
}
-> exec { 'Append IdentityFile':
  command => '/usr/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
-> exec { 'Append PasswordAuthentication':
  command => '/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
