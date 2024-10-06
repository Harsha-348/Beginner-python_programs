# program to find fibonacci sequence of particula range:

for series in range(0,50+1):
    if series == 0:
        print(0)
    elif series ==1:
        print(1)
    else:
        print(series= (series-1) + (series-2))
