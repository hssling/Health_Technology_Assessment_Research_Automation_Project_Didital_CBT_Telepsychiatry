# HTA Protocol: Fractional-Dose IPV and Selected Adult Vaccines (Pneumococcal, Influenza) for India

## 1. Background
India’s Universal Immunization Programme (UIP) has primarily focused on under-5 immunization. However, (a) introduction of IPV and its supply/price constraints, and (b) the rising burden of pneumococcal disease and influenza among the elderly, people with comorbidities, and health workers, have created a need to evaluate alternative dosing strategies and adult vaccination. Fractional-dose IPV (fIPV), delivered intradermally, has been shown to provide adequate seroconversion while reducing per-child IPV consumption. WHO and several LMICs have explored fIPV to handle supply and cost constraints. For India, a formal HTA can answer which strategy is best value-for-money:

1. Full-dose IPV for all in schedule;
2. Fractional-dose IPV (2-dose intradermal schedule);
3. Adult vaccination for specific risk groups (pneumococcal, influenza) – whether it should be publicly financed.

## 2. Objectives
- **Primary:** To assess the cost-effectiveness of fractional-dose IPV compared with full-dose IPV in the Indian UIP context.
- **Secondary:**
  - To evaluate the cost-effectiveness of introducing adult pneumococcal and seasonal influenza vaccines for high-risk groups (elderly ≥60, COPD/diabetes, HCWs).
  - To estimate budget impact of switching to fIPV vs continuing full-dose IPV.
  - To identify supply/logistics conditions under which fIPV is clearly preferred.

## 3. PICO
- **Population (Part A):** Children eligible for IPV under UIP.
- **Intervention (Part A):** 2-dose intradermal fractional-dose IPV.
- **Comparator (Part A):** 1- or 2-dose full IPV schedule, intramuscular.
- **Population (Part B):** Elderly (≥60 yrs), high-risk adults (DM, COPD, CVD), and healthcare workers.
- **Intervention (Part B):** Adult pneumococcal (PCV/PPV) and seasonal influenza vaccine.
- **Comparator (Part B):** No adult vaccination (current practice).
- **Perspective:** Government / program perspective (UIP / NHM); secondary societal.
- **Time horizon:** 10 years for program/BIA; lifetime for CEA.
- **Discounting:** 3%.

## 4. Methods
### 4.1 Evidence Review
- Databases: PubMed, Embase, Cochrane, IndMED.
- Keywords: "fractional dose IPV", "intradermal IPV", "pneumococcal vaccine adults India", "influenza vaccine India", "cost-effectiveness", "health technology assessment".
- Grey literature: NTAGI recommendations, MoHFW UIP reports, WHO position papers.

### 4.2 Modelling Approach
**Part A (fIPV):**
- Static cohort model for a birth cohort.
- Compare vaccine acquisition + delivery costs for full-dose vs fractional-dose.
- Adjust for seroconversion/immunogenicity differences (if any).
- Outcome: cost per fully immunized child; cost per case of paralytic polio prevented (very low incidence → scenario-based).

**Part B (Adult Vaccines):**
- Markov / decision-tree for adults with annual risk of pneumonia/influenza.
- Vaccine effectiveness from literature.
- Costs from Indian tertiary centres and published costing.
- Outcome: cost per QALY gained; cost per hospitalization averted.

### 4.3 Sensitivity Analysis
- One-way: vaccine price, wastage, coverage, device/syringe cost, cold-chain cost.
- Scenario: supply-constrained IPV vs cost-saving IPV.
- Scenario: high-risk adult groups only vs mass elderly vaccination.

### 4.4 Budget Impact
- Inputs: annual birth cohort of India; assumed coverage; IPV dose price (full vs fraction); number of high-risk adults.
- Outputs: annual and 5-year budget.

## 5. Outputs
1. Search strategy
2. Data extraction sheet
3. Python model (two parts: fIPV and adult vaccines)
4. BIA CSV
5. Draft manuscript/policy brief
