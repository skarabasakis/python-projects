def _format_prompt(prompt):
    return f'{prompt}: '

def number(prompt):
    x = input(_format_prompt(prompt))
    return int(x)

def string(prompt):
    x = input(_format_prompt(prompt))
    return x

def select(prompt, options):
    options_str = ', '.join([f"({k}) {v}" for k, v in options.items()])
    selections = options.keys()
    x = input(_format_prompt(f"{prompt}: {options_str}. ({'/'.join(selections)})"))
    return options.get(x)
