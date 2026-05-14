# AGENT CAPABILITIES & SKILLS: RF Engineering Talent Intelligence 
**Owner:** Christopher Velasco, CVE Sourcing  
**Target Sectors:** Satellite, Space, 5G mmWave, & Defense 

## 1. CORE OPERATIONAL SKILLS
This agent is a "High-Fidelity" recruiting engine designed to move beyond simple keyword matching into autonomous technical reasoning and ecosystem mapping.

### 1.1 Multi-Source Discovery (RF/Hardware Focus)
* **Deep Ecosystem Mapping:** Autonomous tracking of 50+ key companies (SpaceX, Kuiper, Anduril, etc.) to identify "Talent Clumps" and migration patterns.
* **Community Mapping: Discovers speakers and active participants from MTT-S, APS, SmallSat, and LLVM Dev Meetings to identify community leaders.
* **USPTO Patent Analysis:** Identifying inventors and patent assignees for specific RF IPs (e.g., Q/V-band, Phased Array tiles).

### 1.2 Technical Reasoning & Vetting
* **Pre-Flight Gap Analysis:** Measuring the "Distance" between a candidate’s technical portfolio (Tape-outs, Tooling) and the specific job requirements.
* **Tooling Fluency Verification:** Evaluating a candidate's mastery of **Ansys HFSS, Keysight ADS, Cadence Virtuoso, and CST Microwave Studio**.
* **Technical Screening Generation:** Creating role-specific "Quiz" questions (e.g., "Trade-offs in analog vs. digital beamforming for 16-element arrays") based on the candidate's actual engineering history.

### 1.3 GTM & Commercial Intelligence
* **Design Win Tracking:** Monitoring semiconductor IP licensing wins to identify high-performing Sales and BD leaders in the RFIC space.
* **Commercial Signal Detection:** Analyzing company health indicators (funding rounds, executive churn, and partnership announcements) to determine "poachability."

---

## 2. COMMUNICATION SKILLS: THE "1:1 THESIS"
The agent does not send "spam." It generates a **Technical Peer-Review** style outreach for every high-value lead.

* **Evidence-Based Outreach:** References specific technical contributions, such as IEEE papers or 28 GHz antenna design patents, to create a "Peer-to-Peer" connection.
* **Narrative Continuity:** Connecting a candidate’s career arc (e.g., "From Intel mmWave to SpaceX Starlink") to the specific mission of the hiring company.
* **Value-First Engagement:** Offering market intelligence or ecosystem data to the candidate, ensuring the first touchpoint is high-value even if they are not currently looking.

---

## 3. AUTONOMY LIMITS (Safety Guardrails)
To protect domain health and reputation, the agent operates under these hard limits:
* **Daily Outreach Cap:** Max 35 high-fidelity emails per 24-hour cycle to ensure quality over quantity.
* **Human-in-the-Loop:** All generated "Theses" must be approved by the Founder before the `outreach.js` module executes the send.
* **Platform Rate Limiting:** Strict adherence to LinkedIn and search engine limits (e.g., Max 10 profile views per hour) to maintain account safety.

---

## 4. FUTURE SKILLS (Roadmap)
- [ ] **ATS Sync:** Direct integration with Greenhouse/Lever for automated candidate stage movement.
- [ ] **Comp-Benchmarking:** Real-time compensation velocity tracking for specialized RF and RISC-V roles.
- [ ] **SDR/GitHub Analysis:** Automated evaluation of Software Defined Radio (SDR) implementations and FPGA-based signal processing code.

---

## 5. REPOSITORY QUICK START
```bash
git clone [https://github.com/cve415/rf-engineering-agent.git](https://github.com/cve415/rf-engineering-agent.git)
cd rf-engineering-agent
# Serve the interactive ecosystem map locally
python -m http.server 8000
