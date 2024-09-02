import pandas as pd


def tot_plus(k=0.0, qty_imp=1000):
    """"""
    weight_acum = 0
    cnt1 = 0
    cnt2 = 0
    proc = k
    corr_on = True if proc != 0 else False  # включение корректировки веса
    corr_decr = True if proc < 0 else False  # корректировка в сторону уменьшения
    proc = abs(proc)
    if corr_on:
        part1 = 100 / proc
        part1_round = round(part1)
        part1_drob = part1 % 1
        comp_on = True if part1_drob != 0 else False  # компенсация округления
        if comp_on:
            real_proc = 100 / part1_round
            err_proc = proc - real_proc
            rnd_down = True if err_proc > 0 else False
            part1_error = 100 / abs(err_proc)

    for i in range(qty_imp):
        if corr_on:
            cnt1 += 1
            cnt2 += 1
            if cnt1 >= part1_round:
                cnt1 = 0
                if corr_decr:
                    continue
                else:
                    weight_acum += 1
            # компенсация округления
            if comp_on and cnt2 >= part1_error:
                cnt2 = 0
                # если процент округлён в меньшую сторону то пропускаем
                # если в большую до добавляем
                if rnd_down:
                    continue
                else:
                    weight_acum += 1

        weight_acum += 1
    return weight_acum

data = []
for i in range(-20, 20):
    weight = tot_plus(i, 1000)
    data.append([i, weight, weight / 1000 * 100 - 100])

df = pd.DataFrame(data, columns=["k", "val", "%"])
df