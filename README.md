# ate-fixture-lab — Pogo-Pin JTAG ATE + Python Automation

<p align="center">

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0ea5e9?style=flat-square)](https://aditya0si.github.io/ate-fixture-lab/)
  <img src="https://img.shields.io/badge/time-42s%20vs%204m10s%20(-83%25)-success?style=flat-square" />
  <img src="https://img.shields.io/badge/coverage-98.2%25%20fault-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/probed-54%20nails%20%7C%20100%25%20nets-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/stack-Python%20%2B%20PyVISA%20%2B%20OpenOCD-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/pytest-7%2F7%20PASS-informational?style=flat-square" />
</p>

<p align="center"><i>From hand-probing to fixture: one clamp, 42 seconds, HTML report.</i></p>

### Fixture
54× P75 pogo pins (100mil grid, bottom-only), 3D-printed base (~$22), alignment pins. Maps to pcb-dfm-dft's 54 test points + JTAG chain. PogoMap in `hardware/pogomap.csv`.

### Flow (pytest, 42s)
| Step | Method | Time |
|------|--------|------|
| Continuity | PyVISA DMM | 4.2s |
| Power rails | INA219 I2C | 1.8s |
| JTAG scan | OpenOCD IDCODE | 0.8s |
| Boundary scan EXTEST | BSDL | 6.4s |
| Flash + CRC | SWD + UART | 8.1s |
| PHY loopback | RMII | 5.2s |
| Functional | UART/LED | 15.5s |

Manual = 4m10s → **83% faster**. Fault 98.2%. Requirement traceability 10/10 in `docs/VALIDATION_PLAN.md`.

### Interactive Lab
→ **`viewer.html`** — live dashboard: click "Run ATE" → 7 bars fill in 42s, JTAG chain animates, power rails gauge, pytest HTML preview. Simulated by default (`--simulate`), real via `ASRL4::INSTR` + FT2232H.

→ **`software/ate.py --simulate`** + **`pytest tests -v`** — no hardware needed.

### Files
`hardware/` — fixture.kicad_pcb, pogomap.csv, 3D step  
`software/` — ate.py, jtag_scan.py, power_test.py  
`tests/` — test_board.py (7 tests), conftest.py  
`docs/` — VALIDATION_PLAN.md

---
*Tests pcb-dfm-dft and asic-crc-engine together — the NPI line in a box.*
