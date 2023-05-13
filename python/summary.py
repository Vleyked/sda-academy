def explain_operators():
    return """
    Arithmetic operators +, -, *, **, /, //, %
    + sum
    - minus
    * multiplication
    ** elevation 3**2 ==> 3^2 (square root)
    / division, the result is always a float
    // Floor division
    % Modulus

    Comparison operators ==, !=, <, >, <=, >=
    == Equals
    != Not equals
    < smaller than
    > higher than
    <= smaller or equals
    >= higher or equals

    Assigment =, +=, -=, *=, **=, /=, //=, %=, &=, ^=, |=, <<=, >>=, :=
    = Assigment, normally used to assign a value to a variable
    := Assignment right away
    += or -= or *= or **= Perform a arithmethic operation to the value of a variable
    += or -= or *= or **= Perform a logic operators to the value of a variable

    Identity operators is, is not they are not equal == !=
    Means that you are checking if the memory allocation is the same
    is, is not --> memory adress is the same
    ==, != --> the value of the variable is the same

    and, or, not logical operators
    and --> Both values need to be True to return True
    or -->  A single value is needed to be True to return True
    not --> Returns the contrary of the bool value inputed

    Memebership operators in, not in
    Search if a value is a member of a collection (string or array)
    4 not in [1, 2, 3] --> This operator will search for 4 value inside the [1,2,3]"""


def explain_variables():
    return """
    Variables are buckets to store some data type in memory and acces it later
    Syntax:
    a = 'Hello'
    """


def data_types():
    return """
    All these are Built-in data types
    digits:
        integer
        floating points
        complex numbers
        binary
        hex
    
    strings
    Bool
    objects --> functions and classes intantiated
    collentions:
        list
        set
        dictionaries
        tuples
    """


# def explain_function():
#     ...


# def function_name(input_variable):
#     input_variable = input_variable * 3
#     return input_variable


# print("Hello" == 5)


def foo(input_var):
    print(input_var)
    output_var = input_var + " World!"
    return output_var


print(foo("Hello"))
