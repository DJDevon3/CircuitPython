import board
import digitalio
import adafruit_sdcard
import storage
import os
import time

spi = board.SPI()
# Use board.SD_CS for Feather M0 Adalogger
# cs = digitalio.DigitalInOut(board.SD_CS)
# Or use a digitalio pin like 5 for breakout wiring:
cs = digitalio.DigitalInOut(board.D5)

# Initialize SDCard to SPI bus
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

# Mounts virtual folder "sd" to your CIRCUITPY board.
# Ensure the folder DOES NOT EXIST or it will throw an error.
# vfs is a Virtual File System. An invisible temporary folder, it's not a USB drive.
virtual_root = "/sd"
storage.mount(vfs, virtual_root)

# Volume Information Stats
SD_Card_Size = os.statvfs(virtual_root)
print("\n")
print("SD Card Stats:")
print("===========================")
print("Block Size: ", SD_Card_Size[0])
print("Fragment Size: ", SD_Card_Size[1])
print("Free Blocks: ", SD_Card_Size[3])
print("Free Blocks Unpriv: ", SD_Card_Size[4])
print("Inodes: ", SD_Card_Size[5])
print("Free Inodes: ", SD_Card_Size[6])
print("Free Inodes Unpriv: ", SD_Card_Size[7])
print("Mount Flags: ", SD_Card_Size[8])
print("Max Filename Length: ", SD_Card_Size[9])
if (SD_Card_Size[0] * SD_Card_Size[3] / 1024 / 1024 / 1024) >= 1.0:
    print("Free Space GB: ", SD_Card_Size[0] * SD_Card_Size[3] / 1024 / 1024 / 1024)
if (SD_Card_Size[0] * SD_Card_Size[3] / 1024 / 1024 / 1024) <= 1.0:
    print("Free Space MB: ", SD_Card_Size[0] * SD_Card_Size[3] / 1024 / 1024)
print(SD_Card_Size[0] * SD_Card_Size[3])

    
# Small pause (in seconds) on Stats before File Directory is shown
time.sleep(3.0)
    
def print_directory(path, tabs=0):
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            print_directory(path + "/" + file, tabs + 1)

print("\n")
print("SD Card Files:")
print("===========================")
print_directory(virtual_root)

# Quick help to remove stuff. Directories must be empty before deleted.
# os.remove("/sd/backgrounds/image.bmp")
# os.rmdir("/sd/backgrounds")

# You can run libraries and .py files from the SD card by appending the system path.
# import something_on_the_sd_card
# sys.path.append("/sd")