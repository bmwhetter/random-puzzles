import itertools

listy = ['3','3','8','8']
operations = ['+','-','/','*']


for par in range(5):
    for i in itertools.permutations(listy):
        for j in itertools.product(operations, repeat = 3):
            if par == 0:
                try:
                    b = '('+'('+i[0]+j[0]+i[1]+')'+j[1]+i[2]+')'+j[2]+i[3]
                    a= eval(b)
                except ZeroDivisionError:
                    continue
                if a >23.9 and a <24.1:
                    print('a' +' = ' + b)
            if par == 1:
                try:
                    b = '(' + i[0] + j[0] + i[1] + ')' + j[1] + '(' + i[2] + j[2] + i[3] + ')'
                    a = eval(b)
                except ZeroDivisionError:
                    continue
                if a >23.9 and a <24.1:
                    print('a' +' = ' + b)
            if par == 2:
                try:
                    b = '(' + i[0] + j[0] + '(' + i[1] + j[1] + i[2] + ')' + ')' + j[2] + i[3]
                    a = eval(b)
                except ZeroDivisionError:
                    continue
                if a >23.9 and a <24.1:
                    print('a' +' = ' + b)
            if par == 3:
                try:
                    b =  i[0] + j[0] + '(' + '(' + i[1] + j[1] + i[2] + ')' + j[2] + i[3] + ')'
                    a = eval(b)
                except ZeroDivisionError:
                    continue
                if a >23.9 and a <24.1:
                    print('a' +' = ' + b)
            if par == 4:
                try:
                    b =  i[0] + j[0] + '(' + i[1] + j[1] + '(' + i[2] + j[2] + i[3] + ')' + ')'
                    a = eval(b)
                except ZeroDivisionError:
                    continue
                if a >23.9 and a <24.1:
                    print('a' +' = ' + b)
