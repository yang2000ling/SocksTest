import json
from lib import vmess_config_lib
from lib import ss_config_lib
from lib import trojan_config_lib

CONFIG_TEMP_PATH = './temp/config_tmp.json'


def node_parse(node, in_port):
    """读取节点字典与inbound端口，解析节点类型，返回规则"""
    if node['type'] == 'ss':
        return ss_config_lib.ss_config_gen(node, in_port)
    elif node['type'] == 'vmess':
        return vmess_config_lib.vmess_config_gen(node, in_port)
    elif node['type'] == 'trojan':
        return trojan_config_lib.trojan_config_gen(node, in_port)


def config_gen(config_list):
    """读取规则列表，生成config数据"""
    self_config = json.load(open(CONFIG_TEMP_PATH))
    print('self_config :', self_config)
    for i in config_list:
        print(i)
        self_config["inbounds"].append(i[0]['inbound'])
        self_config["outbounds"].append(i[0]['outbound'])
        self_config["routing"]["rules"].append(i[0]['rule'])
    return self_config


def write_config(config, config_path):
    """读取config数据，xray配置文件路径，写入文件"""
    f_config = open(config_path, 'w+', encoding='utf-8')
    json.dump(config, f_config, ensure_ascii=False)
    print("{0}({1})\n".format("save json success!", config_path))
    f_config.close()


if __name__ == '__main__':
    pass
