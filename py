import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {'Column1': [1, 2, 3, 4, 5], 'Column2': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)


print("Данные:")
print(df)

я
df.plot(x='Column1', y='Column2', kind='line', marker='o')
plt.title('Пример графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()


print("\nСреднее значение Column2:", df['Column2'].mean())
