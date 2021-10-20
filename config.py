from lib import config_lib
from lib import node_lib
import copy

CONF_FILE = '/usr/local/etc/xray/config.json'


def config_list_gen(nodes_list, start_port=10800):
    config_list = []
    in_port = start_port
    try:
        for i in nodes_list:
            node = node_lib.node_decoder(i)
            # print(node)
            if config := config_lib.node_parse(node, in_port):
                config_list.append(copy.deepcopy(config))
                in_port = in_port + 1
            else:
                continue
        xray_config = config_lib.config_gen(config_list)
        config_lib.write_config(xray_config, CONF_FILE)
        return True
    except Exception as error:
        print(error)
        return False


if __name__ == '__main__':
    pass
