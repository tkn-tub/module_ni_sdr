import logging
import datetime
import time
import random
import wishful_upis as upis
from wishful_agent.core import wishful_module
from wishful_agent.timer import TimerEventSender

__author__ = "Anatolij Zubow"
__copyright__ = "Copyright (c) 2016, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{zubow}@tkn.tu-berlin.de"

'''
Local test of R&S module.
'''

@wishful_module.build_module
class NiSDRController(wishful_module.ControllerModule):
    def __init__(self):
        super(NiSDRController, self).__init__()
        self.log = logging.getLogger('NiSDRController')

    @wishful_module.on_start()
    def my_start_function(self):
        self.log.info("start NI-SDR test")

        try:
            node = self.localNode

            iface = 'unset'
            num_packets = 100
            pinter = 1
            numRxPkts = node.net.gen_layer2_traffic(iface, num_packets, pinter)

            self.log.info('No. of received packets: %d' % numRxPkts)

        except Exception as e:
            self.log.error("{} Failed with control of NI-SDR, err_msg: {}".format(datetime.datetime.now(), e))
            raise e

        self.log.info('... done')

    @wishful_module.on_exit()
    def my_stop_function(self):
        self.log.info("stop NI-SDR test")
