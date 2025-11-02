"""Digital CBT / Tele-psychiatry HTA – decision model"""

population = 1000              # people screened positive
adherence = 0.6                # 60% complete dCBT
remission_intervention = 0.55  # 55% of completers remit
remission_usual = 0.25         # 25% remit under usual care

# costs (INR)
app_cost_per_user = 250
counsellor_cost_per_session = 200
avg_sessions = 4
psychiatrist_cost_per_session = 500
prop_need_psychiatrist = 0.2   # 20% escalate
drug_cost_per_patient = 150

def strategy_usual():
    remitted = population * remission_usual
    cost = population * drug_cost_per_patient   # rough
    return remitted, cost

def strategy_digital():
    # people who actually do dCBT
    completers = population * adherence
    remitted_from_dcbt = completers * remission_intervention
    # non-completers fall back to usual care remission
    non_completers = population - completers
    remitted_from_non = non_completers * remission_usual

    total_remitted = remitted_from_dcbt + remitted_from_non

    # costs
    app_cost = population * app_cost_per_user
    counsellor_cost = completers * avg_sessions * counsellor_cost_per_session
    psych_cost = population * prop_need_psychiatrist * psychiatrist_cost_per_session
    drug_cost = population * drug_cost_per_patient

    total_cost = app_cost + counsellor_cost + psych_cost + drug_cost
    return total_remitted, total_cost

if __name__ == "__main__":
    rem_u, cost_u = strategy_usual()
    rem_d, cost_d = strategy_digital()

    incr_cost = cost_d - cost_u
    incr_remission = rem_d - rem_u

    icer_per_case = incr_cost / incr_remission if incr_remission > 0 else None

    print("Usual care – remitted:", rem_u, "cost:", cost_u)
    print("Digital CBT – remitted:", rem_d, "cost:", cost_d)
    print("Incremental cost:", incr_cost)
    print("Incremental remitted cases:", incr_remission)
    print("ICER – cost per additional remission (INR):", icer_per_case)
