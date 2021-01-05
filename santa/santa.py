import random
from collections import namedtuple

child = namedtuple('Child', 'name present color nice')
CHILDREN = [
    child(name='Bob', present='bike', color='blue', nice=True),
    child(name='Mary', present='trumpet', color='pink', nice=True),
    child(name='Alice', present='playstation', color='white', nice=False),
    child(name='Michael', present='skateboard', color='red', nice=False)
]

def main():
    for child in CHILDREN:
        if child.nice:
            present = make_present(child.present, child.color)
            deliver_present(child.name, present)
        else:
            pass

def make_present(present, color):
    painted_present = paint_present(present, color)
    wrapped_present = wrap_present(painted_present)
    return wrapped_present

def paint_present(present, color):
    return f"{color} {present}"

def wrap_present(present):
    wrapping_paper = random.choice(['shiny paper', 'festive paper', 'christmassy paper'])
    return f"{present} wrapped in {wrapping_paper}"

def deliver_present(name, present):
    print(f"You have been nice this year, {name}. Here is a {present} from Santa.")

main()
