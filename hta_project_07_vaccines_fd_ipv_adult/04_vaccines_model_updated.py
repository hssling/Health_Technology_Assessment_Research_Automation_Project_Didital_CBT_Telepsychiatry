"""Vaccines HTA – fractional-dose IPV + adult vaccines
Run two comparisons:
A) fIPV vs full-dose IPV
B) Adult pneumococcal/influenza vs no adult vaccination
Replace placeholder values with real data.
"""

# ---------- PART A: fIPV vs full-dose IPV ----------
birth_cohort = 25000000   # example India annual birth cohort
coverage = 0.85
price_full = 220.0        # INR per full IPV dose
price_fraction = 120.0    # INR per fractional course (2x smaller doses)
delivery_cost = 30.0      # per child

def cost_full_ipv():
    return birth_cohort * coverage * (price_full + delivery_cost)

def cost_fractional_ipv():
    # Assuming 2 intradermal fractional doses per child
    return birth_cohort * coverage * (price_fraction + delivery_cost)

if __name__ == "__main__":
    cost_full = cost_full_ipv()
    cost_frac = cost_fractional_ipv()
    savings = cost_full - cost_frac
    print("=== PART A: IPV ===")
    print("Cost – full-dose IPV (annual):", cost_full)
    print("Cost – fractional-dose IPV (annual):", cost_frac)
    print("Annual savings if switching to fIPV:", savings)

    # ---------- PART B: Adult vaccines ----------
    adult_population = 80000000    # elderly/high-risk
    target_coverage = 0.4
    price_pneumo = 1600.0
    price_influenza = 600.0
    admin_cost = 80.0

    # Baseline incidence (per year) – placeholders
    pneumo_incidence = 0.015   # 1.5%
    influenza_incidence = 0.10 # 10%
    hosp_cost_pneumo = 15000
    hosp_cost_influenza = 5000

    # Vaccine effectiveness
    ve_pneumo = 0.45
    ve_influenza = 0.5

    # Strategy 1: no adult vaccination
    baseline_pneumo_cases = adult_population * pneumo_incidence
    baseline_influenza_cases = adult_population * influenza_incidence
    baseline_cost = baseline_pneumo_cases * hosp_cost_pneumo + baseline_influenza_cases * hosp_cost_influenza

    # Strategy 2: vaccinate target group
    vaccinated = adult_population * target_coverage
    # prevented cases
    prevented_pneumo = vaccinated * pneumo_incidence * ve_pneumo
    prevented_influenza = vaccinated * influenza_incidence * ve_influenza

    vaccine_cost = vaccinated * (price_pneumo + price_influenza + admin_cost)
    residual_pneumo_cost = (baseline_pneumo_cases - prevented_pneumo) * hosp_cost_pneumo
    residual_influenza_cost = (baseline_influenza_cases - prevented_influenza) * hosp_cost_influenza
    total_cost_vaccination_strategy = vaccine_cost + residual_pneumo_cost + residual_influenza_cost

    incr_cost = total_cost_vaccination_strategy - baseline_cost
    total_prevented_cases = prevented_pneumo + prevented_influenza
    icer_per_case = incr_cost / total_prevented_cases if total_prevented_cases > 0 else None

    print("\n=== PART B: Adult Vaccines ===")
    print("Baseline (no adult vaccination) cost:", baseline_cost)
    print("Vaccination strategy cost:", total_cost_vaccination_strategy)
    print("Incremental cost:", incr_cost)
    print("Total cases prevented:", total_prevented_cases)
    print("ICER – cost per case prevented (INR):", icer_per_case)
