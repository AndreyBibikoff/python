import re

with open('text_6.txt', 'r', encoding='utf-8') as init_f:
    for a in init_f:
        a = a.split()
        my_p = a[0][0:-1]
        a.pop(0)
        lst = []
        result = []
        sum1 = 0
        for i in a:
            d = re.compile('[\d]')
            lst.append(''.join(d.findall(i)))
        for i in lst:
            if i != '':
                result.append(int(i))
        for i in result:
            sum1 += i
            vse = [my_p, sum1]
        for line in vse:
            result_dict = {my_p: sum1}
        print(result_dict)
