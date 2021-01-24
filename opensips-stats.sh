#!/bin/bash

# Date:                 24/01/2021
# Author:               Kavin Chauhan
# Description:          A script to send Opensips stats to zabbix server by using zabbix sender
# Requires:             Zabbix Sender, zabbix-opensips.py

get_OpenSIPs_metrics(){
python3 /usr/local/bin/zabbix-opensips.py
}

# Send the results to zabbix server by using zabbix sender
result=$(get_OpenSIPs_metrics | /usr/bin/zabbix_sender -vv -c /etc/zabbix/zabbix_agentd.conf -i - 2>&1)
response=$(echo "$result" | awk -F ';' '$1 ~ /^info/ && match($1,/[0-9].*$/) {sum+=substr($1,RSTART,RLENGTH)} END {print sum}')
if [ -n "$response" ]; then
        echo "$response"
else
        echo "$result"
fi
