###################################################
# Repeatable timer class for multiple stop starts #
###################################################

#Why the hell is this not built into python?

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
    
	#monitor the timer running
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

	#start the timer
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

	#stop the timer		
    def stop(self):
        self._timer.cancel()
        self.is_running = False
