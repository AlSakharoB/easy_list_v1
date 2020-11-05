def ft_len_mass(mass):
    count = 0
    for i in mass:
        count += 1
    return count


def ft_rev_list(mass):
    return mass[ft_len_mass(mass)::-1]


def ft_rshift_list(mass):
    mass.append(mass.pop(0))
    return mass


def ft_super_shift_list(mass, n):
    n = n % ft_len_mass(mass)
    s = 0
    if n >= 0:
        mass = ft_rev_list(mass)
        while s < n:
            mass = ft_rshift_list(mass)
            s += 1
        mass = ft_rev_list(mass)
        return mass
    if n < 0:
        n = -n
        while s < n:
            mass = ft_rshift_list(mass)
            s += 1
        return mass
