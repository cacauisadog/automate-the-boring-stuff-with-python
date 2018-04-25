def comma_code(list):
    result = ''
    for i in range(len(list)):
        if i == (len(list) - 1):
            result += 'and %s' % list[i]
        else:
            result += '%s, ' % list[i]
    return result

dani = ['linda', 'gostosa', 'cheirosa', 'maravilhosa']
print('A Dani é o que?')
print(comma_code(dani))
