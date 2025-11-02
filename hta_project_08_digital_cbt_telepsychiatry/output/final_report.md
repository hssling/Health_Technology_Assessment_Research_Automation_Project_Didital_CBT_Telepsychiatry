# HTA Automation Report – hta_project_08_digital_cbt_telepsychiatry

**Generated:** 2025-11-02 15:19:30

## 1. Protocol (parsed)
# HTA Protocol: Digital CBT and Tele-Psychiatry for Common Mental Disorders at PHC / HWC Level in India

## 1. Background
Common mental disorders (CMDs) such as depression, anxiety, and somatoform disorders are prevalent in India, but detection and treatment gaps remain high, especially in rural and underserved areas. The Government of India has launched the National Tele-Mental Health Programme (Tele-MANAS) and is integrating mental health services into Ayushman Bharat – HWCs. At the same time, there is rapid growth of **digital CBT (dCBT)**, app-based therapy, and hub-and-spoke tele-psychiatry models. An HTA is needed to determ...

## 2. Objectives
**Primary objective:**
- To compare the cost-effectiveness of (a) digital CBT / tele-psychiatry–assisted care vs (b) usual facility-based mental health care (or no structured care) for mild to moderate depression/anxiety at PHC/HWC level.

**Secondary objectives:**
- To estimate the budget impact of scaling Tele-MANAS–style services to one district/state.
- To determine the threshold at which per-user platform cost makes dCBT cost-saving.
- To explore stepped-care models (self-help → dCBT → tele-psychiatry).

## 3. PICO
- **Population:** Adults (15–60 years) attending PHCs/HWCs with mild to moderate depression/anxiety (PHQ-9 / GAD-7 screened positive).
- **Intervention:** Digital CBT app (smartphone/web) + remote counsellor/tele-psychiatry backup (Tele-MANAS style).
- **Comparator:** Usual care (sporadic counselling, pharmacotherapy when available, or no treatment).
- **Outcomes:** Symptom remission/improvement, QALYs gained, productivity days gained, suicidal ideation reduction.
- **Perspective:** Government health system; secondary societal (productivity).
- **Time horizon:** 1 year (base case), 5 years (sensitivity).
- **Discounting:** 3% for >1 year.

## 4. Methods
- Decision tree for 1-year episode of CMD:
  - Screen positive → offered dCBT → adherence vs non-adherence → clinical improvement vs no improvement → resource use.
  - Usual care branch with lower uptake and lower improvement.
- Effectiveness inputs from RCTs / implementation studies on dCBT / tele-mental health in LMICs.
- Costs: app/platform license, data package, counsellor time, psychiatrist tele-consult, supervision, medicines.
- Outcome: cost per additional case recovered; cost per QALY gained.

## 5. Sensitivity / Scenario Analysis
- One-way: app cost per user, adherence rate, counsellor salary, number of tele-consults, baseline remission under usual care.
- Scenario: district-level hub-and-spoke (1 psychiatrist → 5–10 PHCs).
- Scenario: low-connectivity / low-smartphone-ownership areas (requires hybrid model).

## 6. Budget Impact
- Inputs: adult population of district, CMD prevalence, expected uptake, app cost, HR cost.
- Output: annual budget for state NHM / DMHP.

## 7. Outputs
1. Search strategy
2. Evidence/extraction sheet (effectiveness, app cost, HR cost)
3. Python decision model
4. BIA sheet/CSV
5. Draft manuscript/policy brief (for NMHP / Tele-MANAS)


## 2. Search Strategy
PubMed search:
(("depression"[Mesh] OR "anxiety disorders"[Mesh] OR depression OR anxiety OR "common mental disorders")
AND ("internet-based cognitive therapy" OR "digital CBT" OR "computerized CBT" OR tele-psychiatry OR telepsychiatry OR telemedicine)
AND (India OR "low- and middle-income countries" OR LMIC)
AND (cost OR "cost-effectiveness" OR "health technology assessment" OR HTA OR "economic evaluation"))
AND ("2005/01/01"[Date - Publication] : "3000"[Date - Publication])

Grey literature:
- Tele-MANAS programme documents
- NMHP guidelines
- WHO mhGAP materials


## 3. Model Output (stdout)
```
Usual care – remitted: 250.0 cost: 150000
Digital CBT – remitted: 430.0 cost: 980000.0
Incremental cost: 830000.0
Incremental remitted cases: 180.0
ICER – cost per additional remission (INR): 4611.111111111111

```

## 4. Draft Manuscript (template)
# Draft Manuscript – Cost-Effectiveness of Digital CBT / Tele-Psychiatry for CMDs in India

## Title
Cost-Effectiveness of Digital Cognitive Behaviour Therapy and Tele-Psychiatry for Common Mental Disorders at the Primary Care Level in India: A Model-Based HTA

## Abstract
...

## Sections
1. Introduction – CMD burden, treatment gap, Tele-MANAS
2. Methods – decision model, adherence, costs, outcomes
3. Results – incremental cost per remission
4. Discussion – integration with NMHP, scalability, digital divide
5. Conclusion


## 5. Orchestrator Log
```
=== Processing project: hta_project_08_digital_cbt_telepsychiatry ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 9 data points.
Data processing: starting...
Data processing: completed, filled 9 rows.
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

Model: executed 04_digital_cbt_model.py
Model stdout:
Usual care – remitted: 250.0 cost: 150000
Digital CBT – remitted: 430.0 cost: 980000.0
Incremental cost: 830000.0
Incremental remitted cases: 180.0
ICER – cost per additional remission (INR): 4611.111111111111

Manuscript generation: starting...
Manuscript generation: completed.
```