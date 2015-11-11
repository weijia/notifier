import logging
import os
import sys
import time
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_path, "libtool"))
print sys.path
from libtool.libtool import append
append("iconizer")
print sys.path

from iconizer.iconizer_consts import ICONIZER_SERVICE_NAME
from iconizer.msg_service.msg_service_interface.msg_service_factory_interface import MsgServiceFactory
import win32com.client

__author__ = 'weijia'


class OutlookChecker(object):
    def __init__(self):
        f = MsgServiceFactory()
        self.msg_service = f.get_msg_service()
    def notify(self, msg):
        self.msg_service.send_to(ICONIZER_SERVICE_NAME, {"command": "notify", "msg": msg})

    def get_folder(self):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        target_folder_index = None
        for i in range(1, 100):
            #Admin
            #print unicode(outlook.Folders.Item(i).Name).encode("gbk", "replace")
            if "GlobalAdmin" in outlook.Folders.Item(i).Name:
                print i
                target_folder_index = i
                break
                #Inbox
        
        print outlook.Folders.Item(target_folder_index).Folders.Item(6).Name

        #Inbox
        return outlook.Folders.Item(target_folder_index).Folders.Item(6)
        
def main():
    o = OutlookChecker()
    o.notify("Started")
    last_mail_subject = None
    inbox = o.get_folder()
    while True:
        #The latest email subject will be shown
        new_subject = inbox.Items.GetFirst().subject
        if last_mail_subject!=new_subject:
            o.notify("New mail:" + new_subject)
            last_mail_subject = new_subject
        time.sleep(60*5)
        


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
