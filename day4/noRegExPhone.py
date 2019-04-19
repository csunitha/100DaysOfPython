

def findPhoneNumber(phone_number):
    start = phone_number.find('(')
    start = start + 1
    end = start +3

    area_code = phone_number[start:end]
    print('area code is ' + area_code)

if __name__ == '__main__':
    findPhoneNumber('Home (555) 265-2901')
    findPhoneNumber('Cell (mobile): (555)-918-8271')
