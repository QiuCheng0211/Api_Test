import socket


class GetIp:
    """ 获取本机ip地址 """

    @staticmethod
    def get_ip():
        # 获取本机计算机名称
        hostname = socket.gethostname()
        print(hostname)
        # 获取本机ip
        ip = socket.gethostbyname(hostname)
        return ip


if __name__ == '__main__':
    print(GetIp.get_ip())
