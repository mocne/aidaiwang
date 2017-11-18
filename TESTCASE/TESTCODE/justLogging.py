# -*- coding: utf-8 -*-

from time import sleep
from BASE import log2file

logger = log2file.logging2logfile()

def startLog():
    i = 1
    while 1:
        logger.info(msg='Just testing logging function running alright for %s times' % str(i))
        i += 1
        sleep(5)

if __name__ == '__main__':
    startLog()