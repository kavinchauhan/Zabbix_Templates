#!/usr/bin/env python
import os
import subprocess as sp

class OpenSIPs(object):
    def __init__(self):
        self.__metrics = []

    def opensipsdata(self):
        output = sp.getoutput('/bin/netstat -pan | grep rtpengine | wc -l')
        self.add_metrics("osips.rtp.sockets" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo dlg_list | grep ID= | wc -l')
        self.add_metrics("osips.call.active" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo uptime | cut -d " " -f3 | tail -n 1')
        self.add_metrics("osips.uptime" ,output)
        output = sp.getoutput("/usr/local/sbin/opensipsctl fifo get_statistics all | tr '\n' '\t'")
        self.add_metrics("osips.allstats" ,output)
    def add_metrics(self, k, v):
        """add each metric to the metrics list"""
        dict_metrics = {}
        dict_metrics['key'] = k
        dict_metrics['value'] = v
        self.__metrics.append(dict_metrics)

    def print_metrics(self):
        """print out all metrics"""
        metrics = self.__metrics
        for metric in metrics:
            zabbix_item_key = str(metric['key'])
            zabbix_item_value = str(metric['value'])
            print('- ' + zabbix_item_key + ' ' + zabbix_item_value)

if __name__ == '__main__':
    opensips = OpenSIPs()
    opensips.opensipsdata()
    opensips.print_metrics()
