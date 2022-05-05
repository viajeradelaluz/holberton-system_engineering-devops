# Increments the Nginx default ULIMIT

exec { 'Update nginx-ULIMIT':
  command => "sed -i 's/-n 15/-n 15000/' /etc/default/nginx && sudo service nginx restart",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
