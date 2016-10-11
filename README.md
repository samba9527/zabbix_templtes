# zabbix_templtes
# 2016年10月11号更新对于unbound运行的检测，参考URL如下：
#

1:在Disk 模板中添加下边的宏

{#DMNAME}    @Linux disks for autodiscovery



2:需要在zabbix的模板Filters 中套用 Administration--General---Regular expressions 中添加正则的匹配，格式如下


Linux disks for autodiscovery   ^(sda|sdb|sdc|xvda|xvdb|xvdc)$  [Result is TRUE]

Process Port for discovery     ^[0-9]{2,}   [Result is TRUE]

3:在zabbix的客户端配置文件customer_define.conf中添加如下。

#unbound process check
UserParameter=net.tcp.listen.unbound[*],grep -q `printf '%04X.00000000:0000.0A' $1` /proc/net/tcp && echo 1 || echo 0

# tcp port discovery
UserParameter=discovery.ports,sudo python /tol/app/zabbix/etc/zabbix_agentd.conf.d/discover_tcp_port.py
