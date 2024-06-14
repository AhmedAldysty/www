import logging
import time
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.transaction import ModbusSocketFramer
from pymodbus.datastore import ModbusSequentialDataBlock

#time.sleep(6)
logging.basicConfig(filename='modbus_server2.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def run_modbus_server():
    # Initialize store for server context
    coils = ModbusSequentialDataBlock(0, [False]*1000)  # 1000 coils
    holding_registers = ModbusSequentialDataBlock(0, [0]*1000)  # 1000 holding registers
    # Initialize discrete inputs and input registers if needed
    discrete_inputs = ModbusSequentialDataBlock(0, [False]*1000)  # 1000 discrete inputs
    input_registers = ModbusSequentialDataBlock(0, [0]*1000)
    store1 = ModbusSlaveContext(di=discrete_inputs, co=coils, hr=holding_registers, ir=input_registers)
    #store2 = ModbusSlaveContext(di=discrete_inputs, co=coils, hr=holding_registers, ir=input_registers)
    context = ModbusServerContext(slaves={0x01: store1}, single=False)

    # Identity for Modbus Server
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '1.0'
    logging.info("Starting Modbus server")
    # Run TCP server
    StartTcpServer(context = context, identity=identity, address=("localhost", 502), framer=ModbusSocketFramer)

if __name__ == "__main__":
    run_modbus_server()




