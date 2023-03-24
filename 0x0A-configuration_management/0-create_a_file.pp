#A manifest file to create a file

file {'/tmp/school':
ensure  =>file,
content =>"I love Puppet\n",
owner   =>'www-data',
mode    =>'0744',
group   =>'www-data',
}
