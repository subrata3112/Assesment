def series_builder(n):
    series = [2,]
    adder=1
    for i in range(1,n):
        series.append(series[i-1]+adder)
        if i%2!=0:
            adder+=6
        else:
            adder-=2

    return series

print(series_builder(9))
## Put n=9 to get the 9 numbers in series
