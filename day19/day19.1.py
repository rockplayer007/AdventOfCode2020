import re

gram, msg = open('input.txt').read().split('\n\n')

grammar = {}
for line in gram.split('\n'):
    first = line.split(':')[0].strip()
    rules = line.split(':')[1].split('|')

    all_rules = []
    for rule in rules: # rule = " 3 4 "
        temp_rule = []
        for r in rule.strip().split(' '):
            temp_rule.append(r)
        all_rules.append(temp_rule)
    grammar[first] = all_rules


def create_regex(start='0'):
    current_string = ''
    for rules in grammar[start]: # ['2','4']

        for rule in rules: # '2'

            if '"' in rule:
                current_string += rule.replace('"', '')
                return current_string
            else:
                current_string += create_regex(rule)
        if grammar[start].index(rules) < len(grammar[start]) - 1:
            current_string += '|'
    return '(' + current_string + ')'


re_string = create_regex()
r = re.compile(re_string)
counter = 0
for m in msg.split('\n'):
    if r.fullmatch(m):
        counter += 1

print(counter)
