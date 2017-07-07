import Pi_Uno_I2C.py

comm=Pi_Uno_I2C()
add=0x04
while True:
    time.sleep(0.1)
    comm.write_info(add,"ABCDEFGH")
    comm.read_info(add)

