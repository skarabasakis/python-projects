from util import *

display.bordered('Census Questionnaire')

members_count = answer.number('How many people live in your household?')
members = []

for i in range(members_count):
    display.underlined(f'Member {i+1}')
    members.append({
        'Name': f'''{answer.string('Last Name')}, {answer.string('First Name')}''',
        'Sex': answer.select('Sex', {'m': 'Male', 'f': 'Female'}),
        'Employment': answer.select('Employment Status', {'a': 'Full-time', 'b': 'Part-time', 'c': 'Unemployed'})
    })

print(members)
