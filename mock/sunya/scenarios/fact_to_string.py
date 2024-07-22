from sunya import get_actor_str


def fact_to_string(fact):
    bits = []
    for fact_bit in fact:
        if isinstance(fact_bit, str):
            bits.append(fact_bit)
        else:
            bits.append(f"[{get_actor_str(fact_bit)}]")
    return " ".join(bits)
