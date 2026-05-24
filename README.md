# RF Engineering Recruiting Agent

by Christopher Velasco

> **Signal over noise: In 2026, top RF and hardware talent is buried in generic recruiter spam. This agent cuts through it by doing deep technical work — mapping ecosystems (satellite, 5G mmWave, defense), cross-checking portfolios (simulation stacks, tape-outs, patents), and producing outreach that reads like peer review, not blast mail.

---

## Dual-track intelligence

| Track | Focus |
|--------|--------|
| **Engineering deep-scan** |  HFSS, ADS, Virtuoso, and CST fluency, PCB design and layout signals, phased-array and beamforming trade-offs, USPTO and IEEE signals, and tooling-aligned screening questions ready for your hiring team. |
| **Sales, Marketing, GTM** | Design-win and IP licensing patterns, funding and partnership timing, BD and sales leaders tied to RFIC wins |

---

## System architecture

This agent is a specialized **co-worker node** under the CVE Core Harness.

- `agent-settings.json`        # Agent runtime configuration & parameter mappings
- `data-signals/`              # Target companies, hotspots, education signals, vetting rubric
- `docs/`                      # Supplementary engineering reference material & technical documentation
- `TECH_STACK.md`              # Comprehensive tech stack overview and platform integration notes


---

## Our approach: agentic augmentation

We use **agentic augmentation**, not replacement. The stack handles high-volume discovery and first-pass technical framing so the human lead can own relationships, negotiation, and closing.

| AI agent (high-volume discovery) | Human lead (high-stakes relationship) |
|----------------------------------|----------------------------------------|
| Ecosystem mapping (50+ key orgs, conference and community signals) | Empathy and fit (motivations, culture, relocation, comp nuance) |
| Portfolio and tooling vetting (pre-flight gap analysis vs. the role) | Final outreach approval and send timing |
| Commercial timing (churn, funding, design-win intel) | Strategic partnerships and long-term trust with engineering leaders |

---

## Human-in-the-loop (HITL)

The CVE Core Harness enforces a strict HITL protocol:

1. **Validation** — AI-generated technical theses are reviewed by the lead before any send path runs (quality over blast volume; caps on daily outreach).
2. **Ethics guardrails** — No autonomous outreach without a human-verified diversity and compliance check; platform rate limits respected to protect accounts.
3. **Correction loop** — Human feedback on vetting accuracy feeds back into `data-signals/` (including the RF vetting rubric) to refine domain behavior.

---

## Quick start

```bash
# 1. Clone this repo
git clone https://github.com/cve415/rf-engineering-agent.git
cd rf-engineering-agent

# 2. Configure (ensure Core Harness is installed)
cp .env.example .env

# 3. Launch tactical dashboard preview
python3 -m http.server 8000
```

---

## Author

**Christopher Velasco** — agentic architecture and technical talent engineering.
