# This Puppet manifest creates a file at /tmp/school
# with specific owner, group, permission and content.

file {'/tmp/school':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
