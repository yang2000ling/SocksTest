import requests
import time


def get_request_time(proxies, test_url='https://www.google.com/generate_204'):
    """测试真链接延时,单位：ms"""
    try:
        r = requests.get(test_url, timeout=3, proxies=proxies)
        if r.status_code == 204:
            t = r.elapsed.total_seconds() * 1000
            return int(t)
        else:
            return False
    except requests.exceptions.Timeout as error:
        # print(error)
        return 'time out'
    except Exception as error:
        # print(error)
        return False


def get_request_speed(proxies):
    """测试真链接延时,单位：m/s"""
    try:
        t_start = time.time()
        with requests.get('http://cachefly.cachefly.net/10mb.test',
                          timeout=(3.05, 15),
                          proxies=proxies,
                          stream=True) as respond:
            content_len = respond.headers.get('content-length')
            print('测试总字节数{}'.format(content_len))
            time_list = [time.time()]
            counter = 0
            for chunk in respond.iter_content(int(int(content_len) / 20)):
                counter = counter + 5
                time_list.append(time.time())
                cost_time = round((time_list[-1] - time_list[-2]), 2)
                print('已测试{}%，耗费{}秒。'.format(counter, cost_time))
                if cost_time > 10:
                    respond.close()
                    return 'time out'
            t = respond.elapsed.total_seconds()
            t_end = time.time()
        speed = 10 / ((t_end - t_start) - t)
        # print('download_time:{},request_time:{}'.format(t_end - t_start, t))
        return round(speed, 3)
    except requests.exceptions.Timeout as error:
        print(error)
        return 'time out'
    except Exception as error:
        print(error)
        return False


if __name__ == '__main__':
    pass
