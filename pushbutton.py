import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[2].mode = pyfirmata.INPUT

while True:
    sw = board.digital[2].read()
    if sw is True:
        board.digital[8].write(1)
    else:
        board.digital[8].write(0)
    time.sleep(0.1)
