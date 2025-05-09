g_name = ''
g_vacation_dates = ''


def setup_profile(name, vacation_dates):
    global g_name
    g_name = name
    global g_vacation_dates
    g_vacation_dates = vacation_dates


def print_application_for_leave():
    print('Заявление на отпуск в период ', g_vacation_dates, '. ', g_name, sep='')


def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег.', g_name)


def print_attorney_letter(to_whom):
    print('На время отпуска в период ', g_vacation_dates, ' моим заместителем назначается ', to_whom, '. ', g_name, sep='')


# setup_profile("Иван Петров", "1 июня – 20 июня")
# print_application_for_leave()
# print_application_for_leave()
# print_holiday_money_claim("15 тысяч пиастров")
# print_attorney_letter("Василий Васильев")
