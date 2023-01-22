echo "direccion mac: $(/usr/sbin/arping -c 1 $1 | grep "from" | awk '{print $4}')"
