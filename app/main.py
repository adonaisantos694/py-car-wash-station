class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        result = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(result, 1)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)

        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

        return price

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power

        return round(total, 1)

    def rate_service(self, new_rating: float) -> None:
        new_avg = (
            self.average_rating * self.count_of_ratings + new_rating
        ) / (self.count_of_ratings + 1)

        self.count_of_ratings += 1
        self.average_rating = round(new_avg, 1)
