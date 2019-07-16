def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> str
    Return the flight status (on time, early, delayed)
    for a flight that was stimated to arrive at scheduled_time 
    but now is stimated to arrive at stimated_time.

    Pre-condition: 
    0.0 <= scheduled_time > 24 and 0.0 <= stimated_time > 24 

    >>> report_status(14.5, 14.5)
    'on time'
    >>> report_status(8.0, 7.9)
    'early'
    >>> report_status(18.0, 18.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
