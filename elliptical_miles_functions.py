def get_elliptical_miles(file_name):
    file = open(file_name, 'r+')
    elliptical_miles = file.read()
    if elliptical_miles is '':
        file.close()
        return elliptical_miles
    else:
        elliptical_miles = float(elliptical_miles)
        file.close()
        return elliptical_miles


def set_elliptical_miles(time, file_name):
    writable_time = str(time)
    file = open(file_name, 'w+')
    file.write(writable_time)
    file.close()

def clear_file_contents(filename):
    file = open(filename, 'w+')
    file.close()