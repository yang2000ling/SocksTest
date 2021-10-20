import re
import requests
import socket
import time


def sleep(sleep_time):
    """延时函数（单位：秒）"""
    print('休眠:' + str(sleep_time) + 's')
    time.sleep(sleep_time)
    print('休眠结束。')


def write_log(str_log, file_name='out_log.txt'):
    """str_log写入信息,file_name为日志文件名"""
    str_time2s = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    f = open(file_name, 'a', encoding='utf-8')
    f.write(str_time2s + " :" + str(str_log) + '\n')
    f.close()


def get_my_ip():
    """获取自身ip"""
    try:
        text = requests.get('http://txt.go.sohu.com/ip/soip', timeout=15).content.decode()
        ip = re.findall(r'\d+.\d+.\d+.\d+', text)[0]
        if ip:
            print(ip)
            return ip
        else:
            print('error getip.')
            return 1
    except Exception as error:
        print('error getip.')
        write_log('get_my_ip:' + str(error))
        return 1


def get_dns_ip(dnsName):
    """获取域名IP"""
    try:
        r = socket.gethostbyname_ex(dnsName)
        dns_ip = r[2][0]
        print(dns_ip)
        if dns_ip:
            return dns_ip
        else:
            return 1
    except:
        return 1
