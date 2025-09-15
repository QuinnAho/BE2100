# Probability calculator for 2.3.8 and 2.4.6

def problem_2_3_8():
    print("---- Problem 2.3.8 ----")
    # Table values
    HH = 70  # High Scratch & High Shock
    HL = 9   # High Scratch & Low Shock
    LH = 16  # Low Scratch & High Shock
    LL = 5   # Low Scratch & Low Shock
    total = HH + HL + LH + LL

    # Events:
    # A = High Shock Resistance
    # B = High Scratch Resistance

    # a) P(A) = High Shock / Total
    P_A = (HH + LH) / total

    # b) P(B) = High Scratch / Total
    P_B = (HH + HL) / total

    # c) P(A') = 1 - P(A)
    P_A_comp = 1 - P_A

    # d) P(A ∩ B) = High Shock AND High Scratch / Total
    P_A_and_B = HH / total

    # e) P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    P_A_or_B = P_A + P_B - P_A_and_B

    # f) P(A' ∪ B) = 1 - P(A ∩ B')
    # B' = Low Scratch, so A ∩ B' = High Shock & Low Scratch = LH
    P_A_comp_or_B = 1 - (LH / total)

    print(f"P(A)       = {P_A:.3f}")
    print(f"P(B)       = {P_B:.3f}")
    print(f"P(A')      = {P_A_comp:.3f}")
    print(f"P(A ∩ B)   = {P_A_and_B:.3f}")
    print(f"P(A ∪ B)   = {P_A_or_B:.3f}")
    print(f"P(A' ∪ B)  = {P_A_comp_or_B:.3f}")


def problem_2_4_6():
    print("\n---- Problem 2.4.6 ----")
    # Table values
    HH = 74  # High Cond & High Strength
    HL = 8   # High Cond & Low Strength
    LH = 15  # Low Cond & High Strength
    LL = 3   # Low Cond & Low Strength
    total = HH + HL + LH + LL

    # a) High conductivity AND High strength
    P_high_both = HH / total

    # b) Low conductivity OR Low strength
    # P(C_low ∪ S_low) = 1 - P(C_high ∩ S_high)
    P_low_cond_or_strength = 1 - P_high_both

    # c) Are low conductivity & low strength mutually exclusive?
    # They are mutually exclusive if P(C_low ∩ S_low) = 0
    mutually_exclusive = (LL == 0)

    print(f"P(C_high ∩ S_high) = {P_high_both:.3f}")
    print(f"P(C_low ∪ S_low)   = {P_low_cond_or_strength:.3f}")
    print("Mutually exclusive?" , "Yes" if mutually_exclusive else "No")


if __name__ == "__main__":
    problem_2_3_8()
    problem_2_4_6()
