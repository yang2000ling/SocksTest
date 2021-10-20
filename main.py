import os
import sys
import config
import speed_test
from lib import xray_util
from lib import node_lib
from lib import lib

NODES_TXT = 'data/nodes.txt'
OUTPUT_TXT = '/home/seele/www/output.txt'
LOG_TXT = 'log.txt'
if __name__ == '__main__':
    os.chdir(sys.path[0])
    while 1:
        try:
            lib.write_log('start main.', file_name=LOG_TXT)
            node_list = speed_test.read_nodes_txt()
            nodes = []
            if config.config_list_gen(node_list):
                xray_util.xray_restart()
                relay_list = speed_test.speed_test(node_list)
                for n in relay_list:
                    nodes.append(n[0])
                print('nodes len:{}'.format(len(nodes)))
                if len(nodes) > 0:
                    sub_text = node_lib.list_to_subscribe(nodes)
                    f = open(OUTPUT_TXT, 'w+', encoding='utf-8')
                    f.write(sub_text)
                    print('write {} ok!'.format(OUTPUT_TXT))
                    f.close()
                else:
                    print('none nodes in list!')
                xray_util.xray_stop()
                lib.write_log('end main.', file_name=LOG_TXT)
                lib.sleep(3600)
            else:
                lib.write_log('config_list_gen error.', file_name=LOG_TXT)
                print('start False!')
                lib.sleep(600)
            continue
        except Exception as error:
            lib.write_log(error, file_name=LOG_TXT)
            lib.sleep(600)
            continue
