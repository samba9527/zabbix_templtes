#!/usr/bin/python
#coding=utf-8
import commands
   
##########返回命令执行结果
def getComStr(comand):
    try:
        stat, proStr = commands.getstatusoutput(comand)
    except:
        print "command %s execute failed, exit" % comand
    #将字符串转化成列表
    #proList = proStr.split("\n")
    return proStr
   
##########获取系统服务名称和监听端口
def filterList():
    tmpStr = getComStr("mount -l -t nfs")
    tmpList = tmpStr.split("\n")
    newList = []
    for i in tmpList:
        val = i.split()
        valTmp = val[2]
        newList.append(valTmp)
    return newList
   
def main():
    netInfo = filterList()
    #格式化成适合zabbix lld的json数据
    json_data = "{\n" + "\t" + '"data":[' + "\n"
    #print netInfo
    for net in netInfo:
        if net != netInfo[-1]:
                json_data = json_data + "\t\t" + "{" + "\n" + "\t\t\t" + '"{#NFSMOUNT}":"' + str(net) + "\"},\n"
        else:
                json_data = json_data + "\t\t" + "{" + "\n" + "\t\t\t" + '"{#NFSMOUNT}":"' + str(net) + "\" }]}"
    print json_data
   
if __name__ == "__main__":
    main()
