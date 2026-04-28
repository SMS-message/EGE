def find_d(
        star1: tuple[float, float],
        star2: tuple[float, float]
):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5




with open("27_A_25364.txt") as f:
    data = tuple(map(lambda x: tuple(map(float, x.split())), f.readlines()))

    cl1, cl2 = [], []

    for star in data:
        if star[1] > 10:
            cl1.append(star)
        else:
            cl2.append(star)

    sky = []
    for cl in cl1, cl2:
        dct = dict()
        for star in cl:
            sumd = 0
            for other_star in cl:
                if star == other_star:
                    continue
                sumd += find_d(star, other_star)
            dct[star] = sumd
        sky.append(dct)

    centers = []
    for cl_ds in sky:
        for key in cl_ds:
            if cl_ds[key] == min(cl_ds.values()):
                centers.append(key)

    print(sorted((find_d(center, (1, 1)) * 10_000 for center in centers)))



with open("27_B_25364.txt") as f:
    data = tuple(map(lambda x: tuple(map(float, x.split())), f.readlines()))

    cl1, cl2, cl3 = [], [], []

    for star in data:
        if star[0] > 20:
            cl1.append(star)
        if star[1] > 22:
            cl2.append(star)
        else:
            cl3.append(star)

    sky = []
    for cl in cl1, cl2, cl3:
        dct = dict()
        for star in cl:
            sumd = 0
            for other_star in cl:
                if star == other_star:
                    continue
                sumd += find_d(star, other_star)
            dct[star] = sumd
        sky.append(dct)

    centers = []
    for cl_ds in sky:
        for key in cl_ds:
            if cl_ds[key] == min(cl_ds.values()):
                centers.append(key)

    q1 = 0
    q2 = 0

    for star in cl3:
        if find_d(centers[2], star) <= 1.2:
            q1 += 1
        if find_d(centers[2], star) <= 0.75:
            q2 += 1

    print(q1, q2)