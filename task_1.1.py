# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Table:
    def __init__(self, material: Union[str], height: Union[int], colour: Union[str]):
        if not isinstance(material, str):
            raise TypeError
        self.material = material

        if not isinstance(height, int):
            raise TypeError
        if not height > 0:
            raise ValueError
        self.height = height

        if not isinstance(colour, str):
            raise TypeError
        self.colour = colour

    def color_change(self, new_color: Union[str]):
        """
        функция изменяет цвет стола
        прим.
        >>> table = Table("дерево", 50, "серый")
        >>> table.color_change("черный")
        """
        ...
    def increasing_height(self, additional_height: Union[int]):
        """
        функция увеличивает высоту стола на additional_height
        прим.
        >>> table = Table("дерево", 60, "серый")
        >>> table.increasing_height(15)
        """
        ...

class Knife:
    def __init__(self, blade_material: Union[str], blade_length: Union[int, float], blade_sharpness: Union[str]):
        if not isinstance(blade_material, str):
            raise TypeError
        self.blade_material = blade_material

        if not isinstance(blade_length, (int, float)):
            raise TypeError
        if not blade_length > 0:
            raise ValueError
        self.blade_length = blade_length

        if not isinstance(blade_sharpness, str):
            raise TypeError
        self.blade_sharpness = blade_sharpness

    def sharpen_knife(self, increase_sharpness: Union[str]):
        """
        функция увеличивает остроту ножа
        прим.
        >>> knife = Knife("углеродистая сталь", 12.5, "плохо наточенный")
        >>> knife.sharpen_knife("острый")
        """
        ...
    def material_change(self, new_material: Union[str]):
        """
        функция меняет материал лезвия ножа
        прим.
        >>> knife = Knife("углеродистая сталь", 12.5, "плохо наточенный")
        >>> knife.material_change("нержавеющая сталь")
        """
        ...

class Orange:
    def __init__(self, moisture_content: Union[int, float], degree_sweetness: Union[str]):
        if not isinstance(moisture_content, (int, float)):
            raise TypeError
        if moisture_content < 0:
            raise ValueError
        self.moisture_content = moisture_content

        if not isinstance(degree_sweetness, str):
            raise TypeError
        self.degree_sweetness = degree_sweetness

    def desiccation(self, decrease_moisture: Union[int, float]):
        """
        функция уменьшает количество влаги в апельсине на decrease_moisture (в процентах)
        прим.
        >>> orange = Orange(50, "кисло-сладкий")
        >>> orange.desiccation(30)
        """
        ...
    def fruit_ripening(self, new_degree_sweetness: Union[str]):
        """
        функция меняет сладость апельсина
        прим.
        >>> orange = Orange(50, "кисло-сладкий")
        >>> orange.fruit_ripening("сладкий")
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass