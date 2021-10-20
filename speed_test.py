from lib import speed_test_lib

NODES_TXT = 'data/nodes.txt'
OUTPUT_TXT = '/home/seele/www/output.txt'


def read_nodes_txt(nodes_txt_path=NODES_TXT):
    node_list = []
    f = open(nodes_txt_path, encoding='utf-8')
    buff = f.read().strip().split('\n')
    for i in buff:
        if len(i) >= 10:
            node_list.append(i)
    return node_list


def speed_test(nodes_list):
    list0 = []
    for i in range(10800, 10800 + len(nodes_list)):
        proxies = {
            'http': 'socks5://127.0.0.1:' + str(i),
            'https': 'socks5://127.0.0.1:' + str(i)
        }
        relay_time = speed_test_lib.get_request_time(proxies)
        print('{}\ncheck request time...{}'.format(nodes_list[i - 10800], relay_time))
        if not relay_time or relay_time == 'time out':
            relay_time = speed_test_lib.get_request_time(proxies)
            print('{}\ncheck request time...{}'.format(nodes_list[i - 10800], relay_time))
        if relay_time and relay_time != 'time out':
            down_time = speed_test_lib.get_request_speed(proxies)
            if down_time and down_time != 'time out':
                list0.append([nodes_list[i - 10800], relay_time, down_time])
                print('port = {},   request_time = {}ms,  request_speed = {}M/s'.format(i, relay_time, down_time))
    list0 = sorted(list0, key=lambda x: x[2], reverse=True)
    return list0


if __name__ == '__main__':
    pass
