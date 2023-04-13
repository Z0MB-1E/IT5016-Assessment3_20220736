def calculate(amount, percent, modifier):
    return (amount * percent / 100) + modifier


def calculate_income_tax(yearly_income):

    # if income is higher than the previous bracket the modifier adds the tax for that portion of income
    # then calculates the remainder with the current brackets percentage
    # the calculate function is called parsing in the parameters for each tax bracket

    if yearly_income <= 14000:
        return calculate(yearly_income - 0, 10.5, 0)

    elif yearly_income <= 48000:
        return calculate(yearly_income - 14000, 17.5, 1470)

    elif yearly_income <= 70000:
        return calculate(yearly_income - 48000, 30, 7420)

    elif yearly_income <= 180000:
        return calculate(yearly_income - 70000, 33, 14020)

    else:
        return calculate(yearly_income - 180000, 39, 50320)


if __name__ == '__main__':
    total_income = float(input("What's your annual income?\n>>> $"))
    tax = calculate_income_tax(total_income)
    print(f"Total tax applicable at ${total_income} is ${tax}")


# I made this as an easy way to roughly estimate how much i should be setting aside for my taxes as I am a contractor
# I plan to add improved functionality in the future to estimate based on weekly income, as well as prompt for
# inputs that are deductable such as donations and certain business expenses. I would also
# like to make tnhe program automatically prompt me at the end of the week to input my income and expenses
