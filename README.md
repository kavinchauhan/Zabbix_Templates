# Zabbix_Templates
Zabbix Opensips template
- First, you have to install python3 and zabbix_sender packages on agent.
    yum install python3 zabbix-sender
- Upload Template_Opensips.xml on your zabbix GUI.
- Create scripts directory in /etc/zabbix/ on zabbix client machine (Agent side).
- Put zabbix-opensips.py, opensips-stats.sh in script location.
- Set everyminute cron using opensips-cron file.
- Use uploaded template on your client host configuration from zabbix UI
