# zabbix_templtes


1:在Disk 模板中添加下边的宏

{#DMNAME}    @Linux disks for autodiscovery



2:需要在zabbix的模板Filters 中套用 Administration--General---Regular expressions 中添加正则的匹配，格式如下


Linux disks for autodiscovery   ^(sda|sdb|sdc|xvda|xvdb|xvdc)$  [Result is TRUE]

Process Port for discovery     ^[0-9]{2,}   [Result is TRUE]


