def ft_even_parts_list(mass):
    list1 = []
    for e in mass:
        if e % 2 == 0:
            list1.append(e)
    return list1
