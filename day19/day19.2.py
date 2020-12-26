import re

gram, msg = open('input.txt').read().split('\n\n')

grammar = {}
for line in gram.split('\n'):
    first = line.split(':')[0].strip()
    rules = line.split(':')[1].split('|')

    all_rules = []
    for rule in rules:  # rule = " 3 4 "
        temp_rule = []
        for r in rule.strip().split(' '):
            temp_rule.append(r)
        all_rules.append(temp_rule)
    grammar[first] = all_rules

# update part2
grammar['8'] = [['8'], ['42', '8']]
grammar['11'] = [['42', '31'], ['42', '11', '31']]

def create_regex(start='0', internal_counter=0):
    if internal_counter > 20:
        return ''
    current_string = ''
    for rules in grammar[start]:  # ['2','4']

        for rule in rules:  # '2'

            if '"' in rule:
                current_string += rule.replace('"', '')
                return current_string
            else:
                if rule == '8':
                    current_string += create_regex('42', internal_counter) + '+'
                else:
                    current_string += create_regex(rule, internal_counter + 1)
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
