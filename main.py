# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def add(x, y):
 """Сложение двух чисел."""
 return x + y

def subtract(x, y):
 """Вычитание двух чисел."""
 return x - y

def multiply(x, y):
 """Умножение двух чисел."""
 return x * y

def divide(x, y):
 """Деление двух чисел."""
 if y == 0:
  return "Деление на ноль невозможно!"
 else:
  return x / y

while True:
 print("Выберите операцию:")
 print("1. Сложение")
 print("2. Вычитание")
 print("3. Умножение")
 print("4. Деление")
 print("5. Выход")

 choice = input("Введите номер операции (1/2/3/4/5): ")

 if choice in ('1', '2', '3', '4'):
  try:
   num1 = float(input("Введите первое число: "))
   num2 = float(input("Введите второе число: "))

   if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

   elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

   elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

   elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

  except ValueError:
   print("Неверный ввод. Пожалуйста, введите число.")

 elif choice == '5':
  break
 else: