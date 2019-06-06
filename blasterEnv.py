#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Apr 12 13:44:33 2019
#========================================
import os
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
BLAST_IMAGE_DIR = os.path.expanduser('~/playblast')

BLAST_IMAGE_FMT = 'tga'



PROCESSOR = os.path.join(os.path.dirname(__file__), 'processor.exe')

PROCESSOR = 'C:/Python27/python.exe {0}'.format(os.path.join(os.path.dirname(__file__), 'processor.py'))

RVIO_BIN  = 'C:/Program Files/Shotgun/RV-7.1.1/bin/rvio_hw.exe'

RV_BIN    = 'C:/Program Files/Shotgun/RV-7.1.1/bin/rv.exe'

FFMPEG_BIN = os.path.join(os.path.dirname(__file__), 'resource/ffmpeg/bin/ffmpeg.exe')




MASK_HEIGHT = 87

MASK_COLOR = (0, 0, 0)



TEXT_FONT  = os.path.join(os.path.dirname(__file__), 'resource', 'font', 'MONACO.TTF')

TEXT_COLOR = (255, 255, 255)

TEXT_BOUND = 12

TEXT_SIZE_UL = 50

TEXT_SIZE_UM = 25

TEXT_SIZE_UR = 25

TEXT_SIZE_DL = 25

TEXT_SIZE_DM = 25

TEXT_SIZE_DR = 50



MOTD_FILE  = os.path.join(os.path.dirname(__file__), 'resource', 'motd', 'Buddha')

VIDEO_FPS  = 24

VIDEO_CODEC = 'libx264'

RV_R_THREADING = 16

RV_W_TRHEADING = 16

AUTO_DELETE_IMAGE = True
