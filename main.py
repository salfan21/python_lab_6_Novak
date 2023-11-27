#1
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Тестові дані
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# Перевірка тестових даних
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#2
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Список, що містить кількість днів у місяцях (лютого може бути 28 або 29)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Перевірка на високосний рік і зміна кількості днів в лютому
    if is_year_leap(year):
        month_days[2] = 29
    else:
        month_days[2] = 28

    # Перевірка валідності значень року та місяця
    if month < 1 or month > 12 or year < 1:
        return None

    # Повернення кількості днів у заданому місяці
    return month_days[month]

# Тестові дані
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

# Перевірка тестових даних
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#3
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        month_days[2] = 29
    else:
        month_days[2] = 28

    if month < 1 or month > 12 or year < 1:
        return None

    return month_days[month]

def day_of_year(year, month, day):
    # Визначення кількості днів у заданому місяці
    days_in_current_month = days_in_month(year, month)

    if days_in_current_month is None or day < 1 or day > days_in_current_month:
        return None  # Невірні аргументи

    # Обчислення сумарної кількості днів у попередніх місяцях
    total_days = sum(days_in_month(year, m) for m in range(1, month))

    # Додавання кількості днів у поточному місяці
    total_days += day

    return total_days

# Тестові дані
test_dates = [
    (2000, 12, 31),  # День 366 у високосному році
    (2022, 2, 28),   # День 59 в звичайному році
    (2021, 2, 29),   # Невірна дата
    (2023, 6, 15)    # День 166 в звичайному році
]

# Перевірка тестових даних
for date in test_dates:
    yr, mo, dy = date
    result = day_of_year(yr, mo, dy)
    print(f"{yr}-{mo:02d}-{dy:02d} -> {result}")

#4
def is_prime(num):
    if num < 2:
        return False  # Від'ємні числа та 0, а також 1, не є простими

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Знайдено дільник, число не є простим

    return True

# Тестування
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#5
def liters_100km_to_miles_gallon(liters):
    gallons_per_liter = 0.264172  # 1 літр ≈ 0.264172 галона
    miles_per_kilometer = 0.621371  # 1 кілометр ≈ 0.621371 милі
    return 1 / ((liters / 100) * gallons_per_liter / miles_per_kilometer)

def miles_gallon_to_liters_100km(miles):
    gallons_per_liter = 0.264172  # 1 літр ≈ 0.264172 галона
    miles_per_kilometer = 0.621371  # 1 кілометр ≈ 0.621371 милі
    return 1 / ((miles / miles_per_kilometer) * gallons_per_liter / 100)

# Тестування
print(liters_100km_to_miles_gallon(3.9))  # Очікувано: 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # Очікувано: 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # Очікувано: 23.52145833333333
print(miles_gallon_to_liters_100km(60.3))  # Очікувано: 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4))  # Очікувано: 7.490910297239916
print(miles_gallon_to_liters_100km(23.5))  # Очікувано: 10.009131205673757

#6
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# Введення значень користувачем
side1 = float(input("Введіть довжину першої сторони: "))
side2 = float(input("Введіть довжину другої сторони: "))
side3 = float(input("Введіть довжину третьої сторони: "))

if is_a_triangle(side1, side2, side3):
    print("Можна побудувати трикутник.")
else:
    print("Не можна побудувати трикутник.")

#7
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    # Знаходимо максимальну сторону
    max_side = max(a, b, c)

    # Застосовуємо теорему Піфагора
    return max_side ** 2 == a ** 2 + b ** 2 + c ** 2 - max_side ** 2


# Введення значень користувачем
side1 = float(input("Введіть довжину першої сторони: "))
side2 = float(input("Введіть довжину другої сторони: "))
side3 = float(input("Введіть довжину третьої сторони: "))

if is_a_right_triangle(side1, side2, side3):
    print("Трикутник є прямокутним.")
else:
    print("Трикутник не є прямокутним або не може існувати.")