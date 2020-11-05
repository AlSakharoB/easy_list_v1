def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_rev_list(mass):
    for i in range(ft_len_mass(mass) - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass
