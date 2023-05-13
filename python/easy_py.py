# Easy task - Complete the logic inside the `circle_area_to_price` function
goal = """Write a program (or function) that will compare 
the area/price ratio between two pizzas. 
In order to calculate the area of a circle P 
at a given radius r - use this formula - Formula.

You have 3 pizza restaurants in your area with different prices and pizza areas, 
enter the appropriate data and answer the question asked in the recommendation.
"""

price1, price2, price3 = 15, 20, 25
radius1, radius2, radius3 = 32, 36, 40


def circle_area_to_price(radius, price):
    # Your code goes here, please don't modify anything else
    # area = pi * (radius^2)
    area = 3.14 * (radius**2)  # Expected 3.14 * (32**2) --> 3215.36
    ratio = area / price  # Expected 214.3573333333334
    return ratio


def recommendation(calculation1, calculation2, calculation3):
    calculation1 = circle_area_to_price(radius1, price1)
    calculation2 = circle_area_to_price(radius2, price2)
    calculation3 = circle_area_to_price(radius3, price3)

    best_pizza = max(calculation1, calculation2, calculation3)

    if best_pizza == calculation1:
        return "The first pizza is the best choice, because it has the highest area/price ratio"

    elif best_pizza == calculation2:
        return "The second pizza is the best choice, because it has the highest area/price ratio"

    return "The third pizza is the best choice, because it has the highest area/price ratio"


def test_solution():
    try:
        assert (
            round(circle_area_to_price(radius1, price1), 2) >= 214.34
            and round(circle_area_to_price(radius1, price1), 2) <= 214.48
        )

        assert (
            round(circle_area_to_price(radius2, price2), 2) >= 203.47
            and round(circle_area_to_price(radius2, price2), 2) <= 203.61
        )

        assert (
            round(circle_area_to_price(radius3, price3), 2) >= 200.96
            and round(circle_area_to_price(radius3, price3), 2) <= 201.10
        )
        assert (
            recommendation(
                circle_area_to_price(radius1, price1),
                circle_area_to_price(radius2, price2),
                circle_area_to_price(radius3, price3),
            )
            == "The first pizza is the best choice, because it has the highest area/price ratio"
        )
    except Exception:  # Bad practice, but I will teach you why it is bad later
        return False
    return True


if __name__ == "__main__":

    circle_area_to_price(32, 15)

    # print(
    #     recommendation(
    #         circle_area_to_price(radius1, price1),
    #         circle_area_to_price(radius2, price2),
    #         circle_area_to_price(radius3, price3),
    #     )
    # )
    # if test_solution():
    #     print("Congratulations! You have completed the task!")
    # else:
    #     print(
    #         """I know you can do it! Be determined, Keep trying!
    #         Tips :)
    #         Formula: https://www.mathsisfun.com/geometry/circle.html,
    #         variables: https://www.w3schools.com/python/python_variables.asp,
    #         Arithmetics operators in Python: https://www.w3schools.com/python/python_operators.asp,
    #         Python functions: https://www.w3schools.com/python/python_functions.asp,

    #         """
    #     )
