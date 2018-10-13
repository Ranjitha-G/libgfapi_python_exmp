import hashlib
from gluster import gfapi
import os

# Create virtual mount
volume = gfapi.Volume('127.0.0.1', 'test')
volume.mount()

for root, dirs, files in volume.walk("/"):
    for filen in files:
        filename = os.path.join(root, filen)
        sha256_hash = hashlib.sha256()
        with volume.fopen(filename,"rb") as f:
            for buf in iter(lambda: f.read(1024), None):
                sha256_hash.update(buf)
            print "Hash for file " + filename + " is: " + sha256_hash.hexdigest()

# Unmount the volume
volume.umount()
