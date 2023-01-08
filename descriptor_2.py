# Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
class Validation:

    def __set__(self, instance, value):
        if type(value) != str:              
            raise TypeError(f'Значение "{self.my_attr}" должно иметь тип str')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Car:
    name = Validation()
    color = Validation()

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        

car_1 = Car('Ford', 'сафари', 80)
print(f'{car_1.name} - цвет {car_1.color}')

car_2 = Car(2, 'опал', 50)
print(f'{car_2.name} - цвет {car_2.color}')

car_3 = Car('Ferrari', 3, 50)
print(f'{car_3.name} - цвет {car_3.color}')