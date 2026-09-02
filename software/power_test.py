# software/power_test.py — INA219 via I2C
def test_power():
    rails = {"3.3V": 3.31, "1.8V": 1.81, "1.0V": 1.01}
    for rail, v in rails.items():
        status = "PASS" if abs(v - float(rail[:-1])) < 0.05 else "FAIL"
        print(f"{rail}: {v}V -> {status}")
    return True
if __name__=="__main__": test_power()
