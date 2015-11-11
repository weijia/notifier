import logging
from iconizer.iconizer_consts import ICONIZER_SERVICE_NAME
from iconizer.msg_service.msg_service_interface.msg_service_factory_interface import MsgServiceFactory

__author__ = 'weijia'


def main():
    f = MsgServiceFactory()
    s = f.get_msg_service()
    s.send_to(ICONIZER_SERVICE_NAME, {"command": "notify", "msg": "hello world"})


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
