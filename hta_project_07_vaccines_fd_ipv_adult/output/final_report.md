# HTA Automation Report – hta_project_07_vaccines_fd_ipv_adult

**Generated:** 2025-11-02 15:19:17

## 1. Protocol (parsed)
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


## 2. Search Strategy
PubMed search:
(("Poliovirus Vaccine, Inactivated"[Mesh] OR IPV OR "fractional dose IPV" OR "intradermal IPV")
AND (India OR "low- and middle-income countries" OR LMIC)
AND (cost OR "cost-effectiveness" OR "health technology assessment" OR HTA OR "budget impact"))
OR
(("pneumococcal vaccines"[Mesh] OR "influenza vaccines"[Mesh])
AND (adult OR elderly OR "high risk")
AND (India)
AND (cost OR "cost-effectiveness" OR HTA))

Grey literature:
- NTAGI reports
- MoHFW UIP reports
- WHO position papers on IPV, pneumococcal, influenza


## 3. Model Output (stdout)
```
=== PART A: IPV ===
Cost – full-dose IPV (annual): 5312500000.0
Cost – fractional-dose IPV (annual): 3187500000.0
Annual savings if switching to fIPV: 2125000000.0

=== PART B: Adult Vaccines ===
Baseline (no adult vaccination) cost: 58000000000.0
Vaccination strategy cost: 119720000000.0
Incremental cost: 61720000000.0
Total cases prevented: 1816000.0
ICER – cost per case prevented (INR): 33986.78414096916

```

## 4. Draft Manuscript (template)
# Draft Manuscript – Cost-Effectiveness of Fractional-Dose IPV and Selected Adult Vaccination in India

## Title
Economic Evaluation of Fractional-Dose IPV and Targeted Adult Vaccination (Pneumococcal and Influenza) for India: A Health Technology Assessment

## Abstract
...

## Sections
1. Introduction – UIP context, IPV supply, adult vaccines neglected
2. Methods – two-part model (child cohort for IPV, adult cohort for vaccines)
3. Results – annual savings from fIPV; ICER for adult vaccination
4. Discussion – policy relevance for NTAGI / MoHFW
5. Conclusion


## 5. Orchestrator Log
```
=== Processing project: hta_project_07_vaccines_fd_ipv_adult ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 4 data points.
Data processing: starting...
Data processing: completed, filled 4 rows.
R: executed.
R stderr:
â”€â”€ Attaching core tidyverse packages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse 2.0.0 â”€â”€
âœ” dplyr     1.1.4     âœ” readr     2.1.5
âœ” forcats   1.0.0     âœ” stringr   1.5.2
âœ” ggplot2   4.0.0     âœ” tibble    3.3.0
âœ” lubridate 1.9.4     âœ” tidyr     1.3.1
âœ” purrr     1.1.0     
â”€â”€ Conflicts â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse_conflicts() â”€â”€
âœ– dplyr::filter() masks stats::filter()
âœ– dplyr::lag()    masks stats::lag()
â„¹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

Model: executed 04_vaccines_model.py
Model stdout:
=== PART A: IPV ===
Cost – full-dose IPV (annual): 5312500000.0
Cost – fractional-dose IPV (annual): 3187500000.0
Annual savings if switching to fIPV: 2125000000.0

=== PART B: Adult Vaccines ===
Baseline (no adult vaccination) cost: 58000000000.0
Vaccination strategy cost: 119720000000.0
Incremental cost: 61720000000.0
Total cases prevented: 1816000.0
ICER – cost per case prevented (INR): 33986.78414096916

Manuscript generation: starting...
Manuscript generation: completed.
```