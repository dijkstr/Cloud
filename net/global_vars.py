# -*- coding: utf-8 -*-

import Queue

# global queues with unlimited queue length
q_send = Queue.Queue(0)
q_recv = Queue.Queue(0)
q_pending = Queue.Queue(0)

recv_buff_size = 8192
