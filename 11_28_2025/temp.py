from typing import List


class PowerSource(object):
    def __init__(self, *args):
        self.args = args

    def get_content(self) -> List:
        return list(self.args)

    def change_content(self, *args) -> None:
        self.args = args

    def voltage(self) -> float:
        return (sum(map(len, filter(lambda x: isinstance(x, str), self.args)))
                +
                sum(filter(lambda x: isinstance(x, int), self.args))) / 10


class ChemicalPowerSource(PowerSource):
    pass


class MechanicalPowerSource(PowerSource):
    pass


class BotanicPowerSource(PowerSource):
    pass


if __name__ == '__main__':
    chem = ChemicalPowerSource("Cuprum", "Zincum", "H2SO4")
    mech = MechanicalPowerSource(22, 31)
    botan = BotanicPowerSource("potato", "Argentum", "Zincum")
    for item in (chem, mech, botan):
        print(*item.get_content())
    botan.change_content("tangerine", "Lithium", "Manganum")
    for item in (chem, mech, botan):
        print(item.voltage())
