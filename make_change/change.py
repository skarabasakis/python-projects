import sys
from decimal import Decimal

DENOMINATIONS_STR = "500 200 100 50 20 10 5 2 1 0.50 0.20 0.10 0.05 0.02 0.01"
DENOMINATIONS = [Decimal(d) for d in DENOMINATIONS_STR.split()]

amount_charged = Decimal(sys.argv[1])
amount_given = Decimal(sys.argv[2])

if amount_charged > amount_given:
    sys.exit("Insufficient amount given.")

remaining_change = amount_given - amount_charged
print(f"Change: {remaining_change}")

change = []
while remaining_change > 0:
    for denomination in DENOMINATIONS:
        if denomination <= remaining_change:
            change.append(denomination)
            remaining_change -= denomination
            break

print(" ".join([str(c) for c in change]))
