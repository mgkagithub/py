def generate_series(N):
    series , p = [] , -6
    for n in range(N):
        term = 2*(3**(2*n))
        term = ' + ' + str(term)
        series.append(term)
        if p < 0 or p == 0:
            series.append(' - {}'.format(abs(p)))
        else:
            series.append(' + {}'.format(abs(p)))
        p += 1
    series_string = ''.join(series)
    return series_string
print(generate_series(iterations:=int(input("Enter the number of iterations: \n")))[3:])