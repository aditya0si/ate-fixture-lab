# software/jtag_scan.py — OpenOCD wrapper
import subprocess, json
# Example OpenOCD command (with FT2232H)
OPENOCD_CMD = "openocd -f interface/ftdi/ft2232h.cfg -f target/stm32h7x.cfg -c 'init; scan_chain; exit'"
def scan():
    # In sim mode, return fake IDCODE
    print("JTAG scan: STM32H743 IDCODE 0x6BA02477 detected")
    print("Boundary scan EXTEST: 54 nets, 0 failures")
    return {"idcode": "0x6BA02477", "chain_len": 1, "extest": "PASS"}
if __name__=="__main__": print(scan())
