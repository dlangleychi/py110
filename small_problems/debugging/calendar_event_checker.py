'''
It is returning the opposite of the correct value - 
it is checking if the date is booked
'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return True

    return False

def is_date_available(date):
    return date not in events

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True