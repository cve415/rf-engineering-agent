# RF Engineering Talent Intelligence — Agent Capabilities

**Owner:** Christopher Velasco, CVE Sourcing  
**Target sectors:** Satellite, Space, 5G mmWave, Defense

This agent is a high-fidelity recruiting engine: it moves beyond keyword matching into technical reasoning and ecosystem mapping for RF and hardware roles.

---

## 1. Core operational skills

### 1.1 Multi-source discovery (RF / hardware)

- **Deep ecosystem mapping:** Autonomous tracking of 50+ key companies (SpaceX, Kuiper, Anduril, etc.) to identify talent clusters and migration patterns.
- **Community mapping:** Surfaces speakers and active participants from MTT-S, APS, SmallSat, and LLVM Dev Meetings to spot community leaders.
- **USPTO patent analysis:** Identifies inventors and assignees for specific RF IP (e.g. Q/V-band, phased-array tiles).

### 1.2 Technical reasoning and vetting

- **Pre-flight gap analysis:** Measures how a candidate’s portfolio (tape-outs, tooling) aligns with the role.
- **Tooling fluency verification:** Evaluates familiarity with **Ansys HFSS**, **Keysight ADS**, **Cadence Virtuoso**, and **CST Microwave Studio**.
- **Technical screening generation:** Role-specific questions (e.g. trade-offs in analog vs. digital beamforming for 16-element arrays) grounded in the candidate’s history.

### 1.3 GTM and commercial intelligence

- **Design win tracking:** Monitors semiconductor IP licensing wins to surface strong sales and BD leaders in RFIC.
- **Commercial signal detection:** Uses funding, executive churn, and partnerships to assess timing and fit.

---

## 2. Communication: the 1:1 thesis

The agent avoids generic outreach. Each high-value lead gets a **technical peer-review** style message.

- **Evidence-based outreach:** Cites concrete contributions (IEEE papers, patents, designs) for a peer-to-peer tone.
- **Narrative continuity:** Links career arcs (e.g. Intel mmWave → SpaceX Starlink) to the hiring company’s mission.
- **Value-first engagement:** Leads with market or ecosystem insight so the first touch is useful even if the person is not actively looking.

---

## 3. Autonomy limits (safety guardrails)

- **Daily outreach cap:** Up to 35 high-fidelity emails per 24 hours (quality over volume).
- **Human in the loop:** Generated theses are approved by the founder before the `outreach.js` send path runs.
- **Platform rate limits:** Respects LinkedIn and search limits (e.g. capped profile views per hour) to protect accounts.

---

## 4. Future skills (roadmap)

- [ ] **ATS sync:** Greenhouse / Lever integration for automated stage updates.
- [ ] **Comp benchmarking:** Compensation velocity for specialized RF and RISC-V roles.
- [ ] **SDR / GitHub analysis:** Review of SDR implementations and FPGA signal-processing code.

---

## 5. Repository quick start

```bash
git clone https://github.com/cve415/rf-engineering-agent.git
cd rf-engineering-agent
# Interactive ecosystem map — open http://localhost:8000 in a browser
python -m http.server 8000
```
