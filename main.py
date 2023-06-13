from datetime import datetime
from application.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(get_employees())
    print(calculate_salary())
    print(datetime.now())