def analysis(hours: float, units: int, productivity: float) -> float:
    """
    The analysis takes into account three parameters, hours, units, and productivity. This analysis compiles data from
    the mywork app to create a score that looks beyond units and productivity. Productivity is only tracked while the
    employee is working and units are being completed. To get a full understanding of employees time and work,
    this analysis provides a score that rewards working a lot of hours, working hard, and working fast.
    :param hours: employee's hours worked for the week.
    :param units: employee's units completed, data accessed from the mywork app.
    :param productivity: employee's productivity for units completed,data accessed from the mywork app.
    :return: This function returns the total score.
    """
    if hours >= 40:
        bonus = 1.25
    elif hours >= 20:
        bonus = 1.05
    else:
        bonus = 1
    overall_units_score = productivity * units
    possible_hours = 100 - hours
    score = overall_units_score / possible_hours
    total_score = score * bonus
    return total_score
