def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_same_parts_list(mass):
    count = 1
    for i in range(ft_len_mass(mass) - 1):
        if mass[i] >= 0 and mass[i + 1] >= 0:
            return True
        if mass[i] < 0 and mass[i + 1] < 0:
            return True
    return False
