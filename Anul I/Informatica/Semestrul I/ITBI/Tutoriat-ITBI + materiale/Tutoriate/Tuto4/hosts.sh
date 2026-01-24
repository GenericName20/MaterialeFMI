#!/bin/bash

# Recomandare: puneti fmi.unibuc.ro in /etc/hosts, la google.com se schimba regulat ip-ul

IP_REGEX="^(([1-9]?[0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))\.){3}([1-9]?[0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))";

IP=""
HOSTNAME=""

while read line; do
    if [[ "$line" =~ $IP_REGEX ]]; then

        words=($line)
        ip=${words[0]}
        host=${words[1]}

	#dig @dns site_cautat +short
        lookup_ip=$(dig "@8.8.8.8" "$host" +short)

        if [[ "$ip" == "$lookup_ip" ]]; then
            echo "$ip ok for $host"
        else
            # Observatie, daca aveti o intrare de tip 127.0.0.1 localhost in /etc/hosts, va aparea bogus
            # E ceva local, nu are sens sa intreb un DNS
            echo "Bogus $ip (for $host)"
        fi;
    fi
done < "/etc/hosts"
