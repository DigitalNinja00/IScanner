echo ""
echo "bytes : $(/usr/bin/ping -c 1 $1 | grep "bytes" | awk '{print $4}')"
echo "$(/usr/bin/ping -c 1 $1 | grep "icmp_seq=" | awk '{print $5}')"
echo "$(/usr/bin/ping -c 1 $1 | grep "ttl=" | awk '{print $6}')" > txt.txt
echo "$(/usr/bin/ping -c 1 $1 | grep "time=" | awk '{print $7}')s"
echo ""
