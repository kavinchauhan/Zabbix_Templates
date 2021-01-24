#!/usr/bin/env python
import os
import subprocess as sp

class OpenSIPs(object):
    def __init__(self):
        self.__metrics = []

    def opensipsdata(self):
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics total_size | cut -d " " -f2')
        self.add_metrics("osips.shmem.total" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics used_size | cut -d " " -f2')
        self.add_metrics("osips.shmem.used" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics real_used_size | cut -d " " -f2')        
        self.add_metrics("osips.shmem.real" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics free_size | cut -d " " -f2')
        self.add_metrics("osips.shmem.free" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics fragments | cut -d " " -f2')
        self.add_metrics("osips.shmem.fragments" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 1xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.1xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 2xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.2xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 3xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.3xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 4xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.4xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 5xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.5xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 6xx_replies | cut -d " " -f2')
        self.add_metrics("osips.sl.6xx_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 2xx_transactions | cut -d " " -f2')
        self.add_metrics("osips.tm.2xx_transactions" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 3xx_transactions | cut -d " " -f2')
        self.add_metrics("osips.tm.3xx_transactions" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 4xx_transactions | cut -d " " -f2')
        self.add_metrics("osips.tm.4xx_transactions" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 5xx_transactions | cut -d " " -f2')
        self.add_metrics("osips.tm.5xx_transactions" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics 6xx_transactions | cut -d " " -f2')
        self.add_metrics("osips.tm.6xx_transactions" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics bad_msg_hdr | cut -d " " -f2')
        self.add_metrics("osips.core.bad_message_header" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics bad_URIs_rcvd | cut -d " " -f2')
        self.add_metrics("osips.core.bad_URIs_rcvd" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics err_replies | cut -d " " -f2')
        self.add_metrics("osips.core.err_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics err_requests | cut -d " " -f2')
        self.add_metrics("osips.core.err_requests" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics fwd_replies | cut -d " " -f2')
        self.add_metrics("osips.core.fwd_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics fwd_requests | cut -d " " -f2')
        self.add_metrics("osips.core.fwd_requests" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics rcv_replies | cut -d " " -f2')
        self.add_metrics("osips.core.rcv_replies" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics rcv_requests | cut -d " " -f2')
        self.add_metrics("osips.core.rcv_request" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics timestamp | cut -d " " -f2')
        self.add_metrics("osips.core.timestamp" ,output)
        output = sp.getoutput('/bin/netstat -pan | grep rtpengine | wc -l')
        self.add_metrics("osips.rtp.sockets" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo dlg_list | grep ID= | wc -l')
        self.add_metrics("osips.call.active" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics unsupported_methods | cut -d " " -f2')
        self.add_metrics("osips.core.unsupported_methods" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics waiting_tcp | cut -d " " -f2')
        self.add_metrics("osips.net.waiting_tcp" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics waiting_tls | cut -d " " -f2')
        self.add_metrics("osips.net.waiting_tls" ,output)
        output = sp.getoutput('/usr/local/sbin/opensipsctl fifo get_statistics waiting_udp | cut -d " " -f2')
        self.add_metrics("osips.net.waiting_upd" ,output)

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
