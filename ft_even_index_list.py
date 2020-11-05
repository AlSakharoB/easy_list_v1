def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_even_index_list(mass):
    mass1 = []
    for i in range(ft_len_mass(mass)):
        if i % 2 == 0:
            mass1.append(mass[i])
    return mass1
