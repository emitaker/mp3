import pyfirmata
import time
import os

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[2].mode = pyfirmata.INPUT

while True:
    sw = board.digital[2].read()
    if sw is True:
        board.digital[8].write(1)
        os.system('vlc music/slowed_reverb/aunque_no_sea_conmigo_slowed_reverb.mp3')
    else:
        board.digital[8].write(0)
    time.sleep(0.1)
