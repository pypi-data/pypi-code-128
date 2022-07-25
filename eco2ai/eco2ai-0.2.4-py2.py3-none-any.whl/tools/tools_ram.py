import psutil
import time


FROM_WATTs_TO_kWATTh = 1000*3600


class RAM():
    """
        This class is the interface for tracking RAM power consumption.
        The RAM class is not intended for separate usage, outside the Tracker class

    """
    def __init__(self, measure_period=10):
        """
            This class method initializes RAM object.
            Creates fields of class object. All the fields are private variables

            Parameters
            ----------
            measure_period: float
                Period of power consumption measurements  in seconds.
                The more period the more time between measurements
                The default is 10

            Returns
            -------

        """
        self._measure_period = measure_period
        self._consumption = 0
        self._start = time.time()


    def get_consumption(self):
        """
            This class method returns RAM power consupmtion amount.

            Parameters
            ----------
            No parameters

            Returns
            -------
            self._consumption: float
                RAM power consumption

        """
        self.calculate_consumption()
        return self._consumption
    

    def _get_memory_used(self,):
        """
            This class method calculates amount of virtual memory(RAM) used.

            Parameters
            ----------
            No parameters

            Returns
            -------
            total_memory_used: float
                Total amount of virtual memory(RAM) used in gigabytes.

        """
        processNames = ['python', 'jupyter']
        list_of_needed_processes = []

        for processName in processNames:
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['name', 'cpu_percent', 'memory_percent'])

                    if processName.lower() in pinfo['name'].lower() :
                        list_of_needed_processes.append(pinfo)
                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

        total_memory = psutil.virtual_memory().total / (1024 ** 3)
        total_memory_used = 0
        for process in list_of_needed_processes:
            total_memory_used += process['memory_percent'] * total_memory / 100
        return total_memory_used


    def calculate_consumption(self):
        """
            This class method calculates RAM power consumption.
            
            Parameters
            ----------
            No parameters
            
            Returns
            -------
            consumption: float
                RAM power consumption
        
        """
        time_period = time.time() - self._start
        self._start = time.time()
        consumption = self._get_memory_used() * (3 / 8) * time_period / FROM_WATTs_TO_kWATTh

        self._consumption += consumption
        # print(self._consumption)
        return consumption