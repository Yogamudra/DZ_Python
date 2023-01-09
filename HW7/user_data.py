def get_info ():
    info = []
    last_name = input('Enter last name: ')
    info.append(last_name)
    first_name = input('Enter first name: ')
    info.append(first_name)
    phone_number = ''
    phone_number = input('Enter phone_number: ')
    info.append(phone_number)
    description = input('Enter description: ')
    info.append(description)
    return info
