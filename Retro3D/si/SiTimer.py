import time



###############################################################################
#
###############################################################################
class SiTimer:

    ###############################################################################
    #
    ###############################################################################
    def __init__(self):

        self.timer_start = time.perf_counter()



    ###############################################################################
    #
    ###############################################################################
    def stop(self):

        timer_end =  time.perf_counter()
        SiLog.KeyVal("time", timer_end - self.timer_start)

