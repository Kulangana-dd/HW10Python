class Validation:

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise TypeError(f'Значение "{self.my_attr}" должно иметь тип int или float')
          
        if value < 0:
            raise ValueError(f'Значение "{self.my_attr}" не может быть отрицательным')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = Validation()
    width = Validation()

    weight = 25      
    thickness = 5
    
    def __init__(self, length, width):
        self.length = length
        self.width = width        

    def asphalt_mass(self):
        res = self.length * self.width * self.weight * self.thickness / 1000
        print (f'Для покрытия дорожного полотна необходимо {res} тонн асфальта')


a = Road(20, 5000)
a.asphalt_mass()

a = Road('двадцать', 5000)
a.asphalt_mass()

# еще пример
# a = Road(20, -5000)
# a.asphalt_mass()