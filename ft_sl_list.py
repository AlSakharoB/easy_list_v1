def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_sl_list(mass):
    prev = mass[0]
    count = 0
    for i in range(ft_len_mass(mass)):
        if mass[i] > prev:
            count += 1
        prev = mass[i]
    return count
