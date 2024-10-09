"""For loops syntax + practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for puppy in pets:
    print(f"Good boy {puppy}!")

names: list[str] = ["Alyssa, Janet, Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
