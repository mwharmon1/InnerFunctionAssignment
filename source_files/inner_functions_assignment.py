"""
Author: Michael Harmon
Last Date Modified: 9/30/2019
Description: This program has a measurements function with 2 inner
functions that will calculate the perimeter and area from a list of numbers
for a square or rectangle..
"""


def measurements(list_1):
    """
    call the area and perimeter functions to calculate perimeter and area
    :param list_1: list of number(s)
    :return: string with perimeter and area result
    """

    def area(list_2):
        """
        calculate the area
        :param list_2: list of number(s)
        :return: the area
        """
        if len(list_2) > 1:
            result_area = 1
            for i in list_2:
                result_area *= i
            return result_area
        else:
            square_area = list_2[0] * list_2[0]
            return square_area

    def perimeter(list_3):
        """
        calculate the perimeter
        :param list_3: list of number(s)
        :return: the perimeter
        """
        if len(list_3) > 1:
            result_perimeter = 0
            for i in list_3:
                result_perimeter += i
            return result_perimeter * 2
        else:
            square_perimeter = list_3[0] * 4
            return square_perimeter

    final_area = area(list_1)
    final_perimeter = perimeter(list_1)
    return "Perimeter = " + str(final_perimeter) + " Area = " + str(final_area)


if __name__ == '__main__':
    print(measurements([0, 0]))
