import logging


# DEBUG:Detailed information , typically of interest only when diagnosing prolems.
# INFO:Confirmation that things are working as expected
# WARNING:An indication that something unexpected happened
# ERROR:Due to a more seruous problem ,the software has not been able to perform some function
# CRITICAL:A serious error, indicating that the program itself may be unable to continue running

def add(x, y):
    return x + y


num_1 = 10
num_2 = 5
add_result = add(num_1, num_2)
logging.warning('Add: {} * {} ={}'.format(num_1, num_2, add_result))
