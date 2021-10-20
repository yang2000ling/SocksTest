trojan_outbound_simple = {
    "tag": "proxy",
    "protocol": "trojan",
    "settings": {
        "servers": [
            {
                "address": "t2.ssrsub.one",
                "method": "chacha20",
                "ota": False,
                "password": "iz3Ndcw8",
                "port": 443,
                "level": 1
            }
        ]
    },
    "streamSettings": {
        "network": "tcp",
        "security": "tls",
        "tlsSettings": {
            "allowInsecure": False
        }
    },
    "mux": {
        "enabled": False
    }
}
trojan_inbound_simple = {
    "tag": "socks",
    "port": 10808,
    "listen": "127.0.0.1",
    "protocol": "socks",
    "settings": {
        "auth": "noauth",
        "udp": True,
        "allowTransparent": False
    }
}
rule_simple = {
    "type": "field",
    "inboundTag": "in10801",
    "outboundTag": "out01"
}


def trojan_config_gen(node, in_port):
    """生成trojan协议inbound_socks_simple, ss_outbound_simple, rule_simple三个规则"""
    inboundTag = 'in' + str(in_port)
    outboundTag = 'out' + str(in_port)
    trojan_outbound_simple['tag'] = outboundTag
    trojan_outbound_simple['settings']['servers'][0]['address'] = node['server']
    trojan_outbound_simple['settings']['servers'][0]['port'] = int(node['port'])
    trojan_outbound_simple['settings']['servers'][0]['password'] = node['password']
    # print(ss_outbound_simple)
    trojan_inbound_simple['tag'] = inboundTag
    trojan_inbound_simple['port'] = in_port
    # print(inbound_socks_simple)
    rule_simple["inboundTag"] = inboundTag
    rule_simple["outboundTag"] = outboundTag
    # print(rule_simple)
    return [{'inbound': trojan_inbound_simple, 'outbound': trojan_outbound_simple, 'rule': rule_simple}]
