import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загружаем данные (замени на свои)
data = {'Column1': [1, 2, 3, 4, 5], 'Column2': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Выводим данные
print("Данные:")
print(df)

# Простая визуализация
df.plot(x='Column1', y='Column2', kind='line', marker='o')
plt.title('Пример графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()

# Простая статистика
print("\nСреднее значение Column2:", df['Column2'].mean())
