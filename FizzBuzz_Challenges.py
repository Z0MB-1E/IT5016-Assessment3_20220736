# fizz buzz is a common challenge for developers, there are many ways to complete this challenge and the solutions
# can say a lot about a developers skill and experience, this demonstrates two different ways
# to complete the challenge


def fizz_buzz():
    # this is representing a basic fizz buzz challenge solution.
    # the for loop here goes between 0 - 101 and performs the following statements for each number
    for num in range(0, 101):

        # the statements take the number and use the modulo to get the remainder to test if each number
        # is divisible by it then prints the correct statement for the calculation
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)


# this is a more advanced version of the fizz fizz_buzz
# buzz challenge, applying more variation with a much broader range of numbers
def fizz_buzz_fuzz_bizz():
    # initializing an empty list for the fizz buzz statements to be appended to
    fizzy_buzzy = []

    # performs the same loop within a range of numbers as the basic fizz buzz challenge
    for num in range(0, 100000):
        # creating an empty string to become the fizz buzz statements
        say = ''

        # uses the modulo to compare each number to all divisors, this will add the corresponding
        # statement to the 'say' string that gets appended to the list and printed at the end of the loop
        if num % 3 == 0:
            say += 'Fizz'
        if num % 5 == 0:
            say += 'Buzz'
        if num % 7 == 0:
            say += 'Fuzz'
        if num % 11 == 0:
            say += 'Bizz'
        if say == '':
            say = num
        fizzy_buzzy.append(say)

    # finally print the list created by fizz buzz fuzz bizz function
    print(fizzy_buzzy)


# individually calling each function to demonstrate how they work within the console
fizz_buzz()
fizz_buzz_fuzz_bizz()

