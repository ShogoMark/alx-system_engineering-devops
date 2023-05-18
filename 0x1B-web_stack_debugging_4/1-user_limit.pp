# puppet conf to allow holberton

exec { 'change_value_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'change_value_to_42':
  command => "/bin/sed -i 's/4/42/g' /etc/security/limits.conf",
}
