def ft_positive_list(mass):
    po_count = 0
    for e in mass:
        if e > 0:
            po_count += 1
    return po_count
