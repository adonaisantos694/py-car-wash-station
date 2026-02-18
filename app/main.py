class Car:
    def __init__(self, brand: str, model: str, year: int, car_type: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.car_type = car_type


class CarWashStation:
    def __init__(self, name: str, location: str, average_rating: float):
        self.name = name
        self.location = location
        # 🔥 CORREÇÃO AQUI: garantir que já nasce arredondado
        self.average_rating = round(average_rating, 1)

    def calculate_washing_price(self, car: Car) -> float:
        prices = {
            "sedan": 20.0,
            "suv": 25.0,
            "truck": 30.0
        }

        return prices.get(car.car_type.lower(), 15.0)

    def wash_single_car(self, car: Car) -> str:
        price = self.calculate_washing_price(car)
        return f"Washing {car.brand} {car.model} costs ${price:.2f}"

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0.0
        for car in cars:
            total += self.calculate_washing_price(car)
        return round(total, 2)

    def rate_service(self, new_rating: float):
        self.average_rating = round(
            (self.average_rating + new_rating) / 2,
            1
        )
