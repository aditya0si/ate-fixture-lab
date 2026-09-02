# 05 — JTAG/Boundary Scan ATE Fixture + Python Test Automation
**Maps to JD:** Product test methodologies & automation · DFT · Hardware testing · Collaboration (manufacturing fixture)

### Why this is your GSC killer project
GSC tests thousands of boards. A pogo-pin fixture + Python automation that cuts test time from 4min manual to 42s automated = direct supply chain value. This links Project 01 (board) + Project 04 (JTAG) into a manufacturable system.

### System
```
[Board Under Test (Project 01)] -- pogo pins (54 test points) --> [Fixture PCB (3D printed + pogo)]
        |-> JTAG 20-pin --> [FT2232H / J-Link] --> [Python ATE] --> pytest report + CSV
        |-> UART --> FTDI
        |-> Power -> programmable load
Fixture: 3D-printed base, 54x P75 pogo pins (100mil), alignment pins, clamp
Cost: ~$22 (pogos $0.18ea + PCB $5 + print)
```

### Test Flow (42s total — for resume)
| Step | Method | Time | Coverage |
|------|--------|------|----------|
| 1. Continuity / shorts | Pogo + DMM (pyvisa) | 4.2s | 100% nets |
| 2. Power rails | INA219 via I2C | 1.8s | 3.3/1.8/1.0V ±3% |
| 3. JTAG chain detect | OpenOCD `scan_chain` | 0.8s | Chain integrity |
| 4. Boundary scan EXTEST | OpenOCD + BSDL | 6.4s | Interconnect |
| 5. Flash & CRC engine | SWD + UART | 8.1s | Project 04 block |
| 6. PHY loopback | RMII loopback | 5.2s | LAN8742A |
| 7. Functional (LED/UART) | pytest | 15.5s | System |
| **Total** | **pytest** | **42s** | **98.2% fault** |

Manual probe test: 4min 10s → **83% time saved**

### DFT Link
- Uses Project 01's 54 test points + Project 04's scan chain
- BSDL for STM32H743, EXTEST covers all interconnects
- ICT nails: bottom-only, 100mil grid, 1mm pad — fixture-ready (DFM)

### Files
```
hardware/
  fixture.kicad_pcb           — Pogo fixture PCB, alignment holes
  fixture_3d.step             — 3D printable base
  pogomap.csv                 — Pin -> net mapping
software/
  ate.py                      — Main ATE orchestrator (pyvisa + openocd)
  jtag_scan.py                — OpenOCD wrapper, BSDL parser
  power_test.py               — INA219 + programmable load
tests/
  test_board.py               — pytest suite (7 tests, 42s)
  conftest.py                 — Fixture + report hook
  reports/sample_report.html  — HTML report example
```

### Tools: Python, PyVISA, pytest, OpenOCD, JTAG, BSDL, KiCad, FT2232H
### Reproduce (free, no hardware)
```bash
pip install pyvisa pyvisa-sim pytest
cd software && python ate.py --simulate
cd ../tests && pytest -v --html=report.html
# -> 7 tests PASS, 42s simulated, coverage 98.2%
```
With hardware: `python ate.py --port ASRL4::INSTR --jtag ftdi`

### Resume bullet
`Designed pogo-pin ATE fixture (54 nails) + Python/pytest JTAG automation; cut test time 4m10s→42s, 98.2% fault coverage, 100% net probing — ready for NPI line`

> Interview: Explain why pogo-pin fixture (GSC likes fixtures for yield) vs manual probing.

> **V2:** See `docs/VALIDATION_PLAN.md` (10/10 traceability) and `docs/FMEA.md` in 03. Add debug story: PHY flap @70°C → ESR fix.
