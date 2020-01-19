def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i
    return peak
