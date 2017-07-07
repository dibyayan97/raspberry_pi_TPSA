import struct
import smbus
import time

#class Pi_Uno_I2C:  
bus = smbus.SMBus(1)
    
##    def uno_addresses(add1,add2,add3,add4):
##        self.add1=add1
##        self.add2=add2
##        self.add3=add3
##        self.add4=add4
        
    
def StringToBytes(val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal

def write_info(address,data_to_send_to_Arduino):
        try:
            bus.write_i2c_block_data(address, 0x00,StringToBytes(data_to_send_to_Arduino))
        except IOError or  UnicodeDecodeError:
            print("IO_Error:I2C slave not detected")

def read_info(address):
        smsMessage = ""
        try:
	    print address	
	    print bus
            data_received_from_Arduino =bus.read_i2c_block_data(address,5,17)
            # print(data_received_from_Arduino)
            # print("---")
            for i in range(len(data_received_from_Arduino)):
                smsMessage += chr(data_received_from_Arduino[i])
    
            #print(smsMessage.encode('utf-8'))
            #print(smsMessage)
       	    return(smsMessage);	
        except IOError or UnicodeDecodeError:
           print("SLAVE NOT DETECTED!")

#comm=Pi_Uno_I2C()
#add=0x04
#while True:
#    time.sleep(0.05)
#    #write_info(add,"ABCDEFGH")
#    reply = read_info(add)	
#    print(reply)
