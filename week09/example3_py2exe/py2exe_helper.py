import os
import sys

def get_main_dir():
    # py2exe'd - works for both scripts and services
    if hasattr(sys, "frozen"):
        return os.path.dirname(sys.executable)
    # Running as a python script based service
    import servicemanager
    if servicemanager.RunningAsService():
        # HACK: last entry on the path seems to be good in this case
        return sys.path[-1]
    # Plain Python script
    return os.path.dirname(sys.argv[0])

