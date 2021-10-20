ss_outbound_simple = {
    "protocol": "shadowsocks",
    "tag": "ss01",
    "settings": {
        "servers": [
            {
                'address': '',
                'port': '',
                'password': '',
                'cipher': ''
            }
        ]
    }
}

inbound_socks_simple = {
    "port": 10811,
    "protocol": "socks",
    "settings": {
        "udp": True
    }
}

inbound_http_simple = {
    "port": 10802,
    "protocol": "http"
}

rule_simple = {
    "type": "field",
    "inboundTag": "in10801",
    "outboundTag": "ss01"
}


def ss_config_gen(node, in_port):
    """生成ss协议inbound_socks_simple, ss_outbound_simple, rule_simple三个规则"""
    inboundTag = 'in' + str(in_port)
    outboundTag = 'out' + str(in_port)
    ss_outbound_simple['tag'] = outboundTag
    ss_outbound_simple['settings']['servers'][0]['address'] = node['server']
    ss_outbound_simple['settings']['servers'][0]['port'] = int(node['port'])
    ss_outbound_simple['settings']['servers'][0]['password'] = node['password']
    ss_outbound_simple['settings']['servers'][0]['method'] = node['cipher']
    # print(ss_outbound_simple)
    inbound_socks_simple['tag'] = inboundTag
    inbound_socks_simple['port'] = in_port
    # print(inbound_socks_simple)
    rule_simple["inboundTag"] = inboundTag
    rule_simple["outboundTag"] = outboundTag
    # print(rule_simple)
    return [{'inbound': inbound_socks_simple, 'outbound': ss_outbound_simple, 'rule': rule_simple}]


if __name__ == '__main__':
    pass
