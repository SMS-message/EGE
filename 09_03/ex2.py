def vaccine_effect(value: int):
    for i, immunoglobulin in enumerate(immunoglobulins):
        if immunoglobulin[-1] < value:
            immunoglobulins[i] = None
    while None in immunoglobulins:
        immunoglobulins.remove(None)


if __name__ == '__main__':
    immunoglobulins = [('IgE', 2), ('IgA', 3),
                       ('IgG', 17), ('IgF', 4),
                       ('IgX', 21), ('IgZ', 5)]
    vaccine_effect(5)
    print(*immunoglobulins, sep='\n')
