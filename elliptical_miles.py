from elliptical_miles_functions import set_elliptical_miles, get_elliptical_miles

filename = 'elliptical_miles.txt'
new_ellptical_time = float(input('Enter the minutes that you were on the elliptical today here: '))
old_ellipitcal_time = get_elliptical_miles(filename)

if old_ellipitcal_time is '':
    set_elliptical_miles(new_ellptical_time, filename)
else:
    total_elliptical_time = old_ellipitcal_time + new_ellptical_time
    set_elliptical_miles(total_elliptical_time, filename)