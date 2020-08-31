'''
Creating a python file which checks for prime or not.
'''
def isprimeornot(num):      
    '''
    Creating a function which checks whether the entered number is prime or not.
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
