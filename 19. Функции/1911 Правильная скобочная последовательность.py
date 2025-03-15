def bracket_check(test_string):
    cntr = 0
    for c in test_string:
        if c == '(':
            cntr += 1
        elif c == ')':
            cntr -= 1
            if cntr < 0:
                cntr = 0
        else:
            return 'NO'
    if cntr == 0:
        return 'YES'
    else:
        return 'NO'

# print(bracket_check("()"))
# print(bracket_check("(()(("))
# print(bracket_check(''))
