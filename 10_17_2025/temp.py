def color_search(*colors_to_find, filename="output.txt"):
    with open("flower_drum.txt") as f:
        colors = []
        for line in f.readlines():
            name, info = line.strip().split("#")
            hex_code, *rgb = info.split()

            name = name.strip()
            hex_code = "#" + hex_code.strip()
            rgb = tuple(map(int, rgb))

            colors.append({"name": name, "hex": hex_code, "rgb": rgb})
    with open(filename, mode="w") as f:
        for color in colors_to_find:
            for info in colors:
                if color == info["name"]:
                    print(color, info["hex"], "\t".join(map(str, info["rgb"])), file=f, sep="\t")
                elif color == info["hex"]:
                    print(color, info["name"], "\t".join(map(str, info["rgb"])), file=f, sep="\t")
                elif color == info["rgb"]:
                    print("\t".join(map(str, info["rgb"])), info["name"], info["hex"], file=f, sep="\t")


import csv

def main():
    with open("alpha_oriona.csv") as f:
        reader = csv.reader(f, delimiter=";")



main()



if __name__ == '__main__':
    # color_search('#F13A13', '#00836E')
    # color_search('Блестящий желтый', 'Воды пляжа Бонди', 'Дыня Крайола', filename='out.txt')

    "alpha_oriona.csv"
