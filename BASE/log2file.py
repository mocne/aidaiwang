# -*- coding: utf-8 -*-

import logging

import time



def logging2logfile():
    logger = logging.getLogger("simple_example")
    logger.setLevel(logging.INFO)
    # 建立一个filehandler来把日志记录在文件里，级别为debug以上
    fh = logging.FileHandler("../../LOGS/mainLog_%s.log" % str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
    fh.setLevel(logging.DEBUG)
    # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # 设置日志格式
    formatter = logging.Formatter("[%(asctime)s][%(pathname)s-%(filename)s-%(module)s-%(funcName)s:%(lineno)d][%(levelname)s] %(message)s")

    '''
    formatter，定义了最终log信息的顺序,结构和内容，用这样的格式 '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'，
    %(name)s Logger的名字
    %(levelname)s 文本形式的日志级别
    %(message)s 用户输出的消息
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(levelno)s 数字形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s  调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    '''

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将相应的handler添加在logger对象中
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger