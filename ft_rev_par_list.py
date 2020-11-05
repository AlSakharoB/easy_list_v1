def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_rev_par_list(mass):
    ch = 0
    for i in range(0, ft_len_mass(mass) - 1, 2):
        ch = mass[i]
        mass[i] = mass[i + 1]
        mass[i + 1] = ch
    return mass
