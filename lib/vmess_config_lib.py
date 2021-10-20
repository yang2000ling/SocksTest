vmess_outbound_simple = {
    "tag": "",
    "protocol": "vmess",
    "settings": {
        "vnext": [
            {
                "address": "123.ocm",
                "port": 1234,
                "users": [
                    {
                        "id": "cc4f8d5b-967b-4557-a4b6-bde92965bc27",
                        "alterId": 0,
                        "security": "aes-128-gcm"
                    }
                ]
            }
        ]
    },
    "streamSettings": {
        "security": "",
        "tlsSettings": {
            "serverName": None
        },
        "wsSettings": {
            "path": None,
            "headers": {
                "Host": None
            }
        },
        "httpSettings": {},
        "network": "tcp",
        "kcpSettings": {},
        "tcpSettings": {},
        "quicSettings": {}
    },
    "mux": {
        "enabled": False
    }
}

inbound_socks_simple = {
    "port": 1080,
    "listen": "127.0.0.1",
    "protocol": "socks",
    "settings": {
        "auth": "noauth",
        "udp": True,
        "ip": "127.0.0.1",
    }
}

rule_simple = {
    "type": "field",
    "inboundTag": "in10801",
    "outboundTag": "ss01"
}


def vmess_config_gen(node, in_port):
    """生成vmess协议inbound_socks_simple, ss_outbound_simple, rule_simple三个规则"""
    inboundTag = 'in' + str(in_port)
    outboundTag = 'out' + str(in_port)
    vmess_outbound_simple['tag'] = outboundTag
    vmess_outbound_simple['settings']['vnext'][0]['address'] = node['add']
    vmess_outbound_simple['settings']['vnext'][0]['port'] = int(node['port'])
    vmess_outbound_simple['settings']['vnext'][0]['users'][0]['id'] = node['id']
    vmess_outbound_simple['settings']['vnext'][0]['users'][0]['alterId'] = int(node['aid'])
    vmess_outbound_simple['settings']['vnext'][0]['users'][0]['security'] = node['scy']
    vmess_outbound_simple['streamSettings']['network'] = node['net']
    vmess_outbound_simple['streamSettings']['security'] = node['tls']
    vmess_outbound_simple['streamSettings']['tlsSettings']['serverName'] = node['host']
    vmess_outbound_simple['streamSettings']['wsSettings']['headers']['Host'] = node['host']
    vmess_outbound_simple['streamSettings']['wsSettings']['path'] = node['path']
    # print(ss_outbound_simple)
    inbound_socks_simple['tag'] = inboundTag
    inbound_socks_simple['port'] = in_port
    # print(inbound_socks_simple)
    rule_simple["inboundTag"] = inboundTag
    rule_simple["outboundTag"] = outboundTag
    # print(rule_simple)
    return [{'inbound': inbound_socks_simple, 'outbound': vmess_outbound_simple, 'rule': rule_simple}]


if __name__ == '__main__':
    pass
