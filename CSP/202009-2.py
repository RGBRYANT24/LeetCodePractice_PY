n, k, t, xl, yd, xr, yu = map(int, input().split())
jingguo = douliu = 0
for i in range(n):
    loc = list(map(int, input().split()))
    count = 0
    is_jingguo = 0
    is_douliu = 0
    flag = False
    for i in range(0, len(loc), 2):
        x, y = loc[i], loc[i + 1]
        if xl <= x <= xr and yd <= y <= yu:
            # print(x, y)
            is_jingguo += 1
            flag = True
            count +=1
            if count >= k:
                is_douliu = 1
        else:
            flag = False
            count = 0
    if is_jingguo:
        jingguo += 1
    if is_douliu:
        # print(count)
        douliu += 1
print(jingguo)
print(douliu)