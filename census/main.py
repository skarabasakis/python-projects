def display_underlined(text, symbol = '-'):
    print()
    print(text)
    print(symbol * len(text))

def display_bordered(text, symbol = '*'):
    print()
    print(symbol * (len(text) + 4))
    print(symbol, text, symbol)
    print(symbol * (len(text) + 4))
    print()

def format_prompt(prompt):
    return f'{prompt}: '

def answer_number(prompt):
    x = input(format_prompt(prompt))
    return int(x)

def answer_string(prompt):
    x = input(format_prompt(prompt))
    return x

def answer_select(prompt, options):
    options_str = ', '.join([f"({k}) {v}" for k, v in options.items()])
    selections = options.keys()
    x = input(format_prompt(f"{prompt}: {options_str}. ({'/'.join(selections)})"))
    return options.get(x)

def main():
    display_bordered('Census Questionnaire')

    members_count = answer_number('How many people live in your household?')
    members = []

    for i in range(members_count):
        display_underlined(f'Member {i+1}')
        members.append({
            'First Name': answer_string('First Name'),
            'Last Name': answer_string('Last Name'),
            'Sex': answer_select('Sex', {'m': 'Male', 'f': 'Female'}),
            'Employment': answer_select('Employment Status', {'a': 'Full-time', 'b': 'Part-time', 'c': 'Unemployed'})
        })

    print(members)

main()
