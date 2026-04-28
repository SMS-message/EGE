from abc import ABC, abstractmethod


class Transport(ABC):
    def delivery(self, cords: tuple[int, int]):
        print(f"[INFO] Delivered by {type(self).__name__}")
        return cords[0] > cords[1]


class Ship(Transport):
    ...


class Truck(Transport):
    ...


class Logistics(ABC):
    def plan_delivery(self):
        transport: Transport = self.create_transport()
        return transport

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


def main():
    sl = SeaLogistics()
    transport = sl.plan_delivery()
    print(transport.delivery((1, 2)))


if __name__ == "__main__":
    main()
