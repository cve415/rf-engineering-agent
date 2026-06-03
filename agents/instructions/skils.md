# SKILL: RF & Hardware Engineering Validation
**Category:** Domain-Specific Technical Vetting
**Target Repository:** `rf-engineering-agent` 

## 1. RADIO FREQUENCY (RF) & MICROWAVE CIRCUIT DEEP SCANNING
The agent possesses the specialized rulesets required to verify implementation-level domain expertise across the electromagnetic spectrum, looking far past shallow "RF" keywords.

### 1.1 Frontend Architecture & Component Analysis
* **Passive & Active RF Design:** Evaluates source-level evidence of low-noise amplifier (LNA) tuning, power amplifier (PA) linearization, mixer architectures, and RF filter networks (SAW/BAW).
* **Impedance Matching & Smith Chart Analytics:** Scans for mathematical or script-based verification of transmission line matching networks ($L$, $\pi$, or $T$ networks) tuned to a strict $50\ \Omega$ standard.

### 1.2 Monolithic Microwave Integrated Circuits (MMIC)
* **Semiconductor Topologies:** Identifies design files and parameters specifying GaAs (Gallium Arsenide), GaN (Gallium Nitride), or SiGe (Silicon Germanium) layouts tailored for high-frequency or high-power operations.

---

## 2. HIGH-SPEED PCB & POWER SYSTEM AUDITING
The agent can audit board-level designs to evaluate physical layout complexity, thermal considerations, and signal integrity constraints.

### 2.1 High-Speed Digital & Mixed-Signal Layout
* **Printed Circuit Board (PCB) Architecture:** Analyzes multi-layer board stackups, differential pair routing constraints, length-matching tolerances, and controlled-impedance trace configurations.
* **Signal & Power Integrity (SI/PI):** Scans for evidence of coplanar waveguide analysis, via stub reduction techniques, decoupling capacitor optimization, and power delivery network (PDN) designs.

### 2.2 Principal Power Board Mechanics
* **Power Conversion Topologies:** Identifies design layouts handling high-efficiency buck/boost regulators, low-dropout (LDO) linear regulators, and custom isolated power supply systems for sensitive analog RF frontends.

---

## 3. ECOSYSTEM HARDWARE-TOOLCHAIN COMPLIANCE
The subagent maps candidate project environments against industry-standard engineering software configurations.

### 3.1 Electronic Design Automation (EDA) Tool Validation
* Scans files and project structures to identify active design dependencies across core hardware tools:
  * **Ansys HFSS / Keysight ADS:** (Advanced Design Systems) for 3D EM simulation and circuit layout.
  * **Altium Designer / Cadence Allegro / KiCad:** For schematic capture, layout topologies, and Gerber file generation.

### 3.2 Laboratory Telemetry & Test Automation
* Identifies integration scripts written for hardware-in-the-loop (HIL) automation platforms, assessing familiarity with instruments like Vector Network Analyzers (VNA), Spectrum Analyzers, and digital oscilloscopes.

---

## 4. RF OUTREACH THESIS CONTEXT GENERATOR
Utilizing the telemetry parsed from the technical signals above, the subagent outputs structured summaries:
* Synthesizes complex hardware achievements (such as optimizing noise figure metrics, mitigating parasitic board capacitance, or designing robust multi-layer stackups) into clear, context-driven validation reports.