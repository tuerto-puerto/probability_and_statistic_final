import pandas as pd

# Загрузка данных
data = pd.read_csv("/content/Ответы на форму.csv")
pd.set_option('display.max_rows', None)
print(data)


print(data['Музыкальные предпочтения'].value_counts())

print(data['Из какого вы региона Кыргызстана?'].value_counts())


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
data['Из какого вы региона Кыргызстана?'].value_counts().plot(kind='bar', color='coral', edgecolor='black')
plt.title("Распределение участников по регионам")
plt.xlabel("Регион")
plt.ylabel("Количество")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import matplotlib.pyplot as plt

# Убедимся, что столбцы корректно загружены
print(data[['Ваш возраст', 'Музыкальные предпочтения']].head())

# Преобразуем данные для удобства анализа
# Присвоим музыкальным предпочтениям числовые значения
data['Музыкальные предпочтения (код)'] = data['Музыкальные предпочтения'].astype('category').cat.codes

# Построим точечный график
plt.figure(figsize=(10, 6))
plt.scatter(data['Ваш возраст'], data['Музыкальные предпочтения (код)'], alpha=0.7, color='orange', edgecolors='black')

# Настройка графика
plt.title("Зависимость возраста от музыкальных предпочтений")
plt.xlabel("Возраст участников")
plt.ylabel("Музыкальные предпочтения (закодировано)")
plt.grid(True, linestyle='--', alpha=0.6)

# Легенда
categories = data['Музыкальные предпочтения'].astype('category').cat.categories
plt.yticks(range(len(categories)), categories)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Проверим данные
print(data[['Ваш возраст', 'Музыкальные предпочтения']].head())

# Создадим сводную таблицу: Частота музыкальных предпочтений по возрастам
pivot_table = data.pivot_table(index='Ваш возраст', columns='Музыкальные предпочтения', aggfunc='size', fill_value=0)

# Построим линейный график
plt.figure(figsize=(12, 6))
pivot_table.plot(kind='line', marker='o', figsize=(12, 6))

# Настройка графика
plt.title("Частота музыкальных предпочтений по возрасту")
plt.xlabel("Возраст")
plt.ylabel("Количество участников")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title="Музыкальные предпочтения", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm 

data = {'Возраст': [25, 30, 22, 28, 35, 27],
        'Пол': ['М', 'Ж', 'М', 'Ж', 'М', 'Ж'],
        'Регион': ['Бишкек', 'Ош', 'Нарын', 'Чуй', 'Ош', 'Иссык-Куль'],
        'Музыка': ['Поп', 'Рок', 'Классика', 'Электронная', 'Рэп', 'Поп']}

df = pd.DataFrame(data)

# Описательная статистика для числовых данных
print(df['Возраст'].describe())

# Анализ распределения возраста
sns.histplot(df['Возраст'], kde=True)
plt.title('Распределение возраста')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('/content/Ответы на форму.csv', encoding='utf-8')

# Просмотр первых нескольких строк данных
print(df.head())

# Пример анализа: Количество респондентов по возрастным группам
age_distribution = df['Ваш возраст'].value_counts()

# Визуализация распределения по возрастным группам
plt.figure(figsize=(10, 6))
age_distribution.plot(kind='bar', color='skyblue')
plt.title('Распределение респондентов по возрастным группам')
plt.xlabel('Возрастные группы')
plt.ylabel('Количество респондентов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Пример анализа: Предпочтения по музыкальным платформам
platforms = df['Какие платформы вы используете для прослушивания музыки?'].str.split(', ').explode().value_counts()

# Визуализация предпочтений по платформам
plt.figure(figsize=(10, 6))
platforms.plot(kind='bar', color='lightgreen')
plt.title('Предпочтения по музыкальным платформам')
plt.xlabel('Платформы')
plt.ylabel('Количество пользователей')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из CSV-файла
df = pd.read_csv('/content/Ответы на форму.csv', encoding='utf-8')

# Просмотр первых нескольких строк данных
print(df.head())

# Подготовка данных для визуализации
# Создаем новый DataFrame, который будет содержать пол и эмоции
emotion_gender = df[['Ваш пол', 'Какие эмоции чаще всего вызывает у вас музыка?']]

# Удаляем строки с пропущенными значениями
emotion_gender.dropna(inplace=True)

# Подсчет количества эмоций по полу
emotion_counts = emotion_gender.groupby(['Ваш пол', 'Какие эмоции чаще всего вызывает у вас музыка?']).size().reset_index(name='Количество')

# Визуализация
plt.figure(figsize=(12, 6))
sns.barplot(data=emotion_counts, x='Ваш пол', y='Количество', hue='Какие эмоции чаще всего вызывает у вас музыка?')
plt.title('Эмоции от прослушивания музыки по полу')
plt.xlabel('Пол')
plt.ylabel('Количество респондентов')
plt.xticks(rotation=45)
plt.legend(title='Эмоции')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из CSV-файла
df = pd.read_csv('/content/Ответы на форму.csv', encoding='utf-8')

# Подготовка данных для визуализации
# Преобразуем категориальные данные в числовые
age_categories = {'до 18': 17, '18–24': 21, '25–34': 30, '35–44': 40, '45–54': 50, '55 и старше': 60}
df['Ваш возраст'] = df['Ваш возраст'].map(age_categories)

# Создаем новый DataFrame, который будет содержать возраст и частоту прослушивания музыки
age_music = df[['Ваш возраст', 'Как часто вы слушаете музыку?']]

# Удаляем строки с пропущенными значениями
age_music.dropna(inplace=True)

# Подготовка данных для построения кривой
# Преобразуем частоту прослушивания в числовые значения
frequency_dict = {'Редко': 1, 'Несколько раз в месяц': 2, 'Несколько раз в неделю': 3, 'Ежедневно': 4}
age_music['Как часто вы слушаете музыку?'] = age_music['Как часто вы слушаете музыку?'].map(frequency_dict)

# Визуализация
plt.figure(figsize=(10, 6))
sns.lineplot(data=age_music, x='Ваш возраст', y='Как часто вы слушаете музыку?', marker='o')
plt.title('Взаимосвязь возраста и частоты прослушивания музыки')
plt.xlabel('Возраст')
plt.ylabel('Частота прослушивания')
plt.tight_layout()
plt.show()