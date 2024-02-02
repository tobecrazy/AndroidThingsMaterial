import pip
from subprocess import call
from importlib import metadata as importlib_metadata
for dist in importlib_metadata.distributions():
    if dist.metadata['Name'] == None :    
        print("============================================")
        print("Incorrect name, will PASS")
        print("============================================")
        pass
    else :
        print("============================================")
        print("Updating for:", dist.metadata["Name"])
        print("============================================")
        call("pip3 --default-timeout=10000 install -U " + dist.metadata["Name"]+ " --break-system-packages", shell=True)
