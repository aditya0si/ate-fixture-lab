# Validation Plan — Requirements → Tests (Traceability Matrix)

| Req ID | Requirement | Test | Method | Pass/Fail Criteria | Data Logging |
|--------|-------------|------|--------|-------------------|--------------|
| PWR-01 | 3.3V ±3% @1.5A transient | Power rail test | INA219 + load step 0->1.5A | 3.201-3.399V, ripple <30mV | CSV + scope PNG |
| PWR-02 | 1.0V ±3% @3A | PDN test | TPS54821 step | 0.97-1.03V, PM>45° | LTspice + bench |
| CLK-01 | 25MHz ±10ppm | Crystal test | Scope freq counter | 24.99975-25.00025MHz | Scope log |
| SI-01 | RMII eye >250mV | SI test | Eye diagram @50MHz | 312mV measured | Eye PNG |
| DFT-01 | JTAG chain | Scan test | OpenOCD IDCODE | 0x6BA02477 | Log |
| DFT-02 | Interconnect | Boundary scan EXTEST | BSDL | 0 failures, 54 nets | BSDL report |
| FUNC-01 | PHY link 100M | Loopback | RMII loopback 1k packets | 0 loss, <2ms latency | pytest log |
| FUNC-02 | CRC engine | ASIC TB | 412 SV tests | 100% line cov | coverage HTML |
| REL-01 | MTBF >100k hrs | Reliability | MIL-HDBK-217 calc | 185k hrs @25°C | FMEA |
| EMC-01 | FCC Part 15 pre-scan | EMC | Near-field probe 30-1000MHz | No spur >6dB margin | Scan CSV |

Automation: All tests in pytest (Project 05), 42s total, HTML report, CSV logs. Requirement coverage: 10/10.
