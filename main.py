from analysis import *


def main() -> None:
    """
    Main function.
    :return: Function returns no data.
    """
    while True:
        name = input('Enter employees first and last name: ').strip().upper()
        hours = float(input('Enter employees hours worked for the week: '))
        exception_handler(hours)
        units = int(input('Enter employees total units for the week: '))
        exception_handler(units)
        productivity = float(input('Enter employees productivity for the week: '))
        exception_handler(productivity)
        employee_analysis(name, hours, units, productivity)

        response = input('Continue (y/n): ').strip().lower()
        if response == 'y':
            continue
        elif response == 'n':
            break
        else:
            while True:
                response = input('Enter y or n: ').strip().lower()
                if response == 'y':
                    break
                if response == 'n':
                    break
        if response == 'n':
            break


def employee_analysis(name: str, hours: float, units: int, productivity: float) -> None:
    """
    This function calls the analysis module for employee work analysis. Then writes all results to a saved file.
    :param name: employee's name.
    :param hours: employee's hours worked for the week.
    :param units: employee's units completed, data accessed from the mywork app.
    :param productivity: employee's productivity for units completed,data accessed from the mywork app.
    :return: This function return no data.
    """
    analysis_score = analysis(hours, units, productivity)
    file = open('output.txt', 'a')
    file.write('{}, {}, {}, {}, {:.2f}'.format(name, hours, units, productivity, analysis_score))
    file.write('\n')
    print('Output Saved.')


def exception_handler(test_input):
    while True:
        try:
            if test_input < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid input')
        test_input = input('Enter non-negative number.: ').strip().lower()


if __name__ == '__main__':
    main()
