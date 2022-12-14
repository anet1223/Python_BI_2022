# re_hw.py

## Устновка

Скопируйте файл *re_hw.py*, *ref.txt* и *2430AD.txt* в отдельную папку.

Для корректной работы скрипта должна быть установлена библиотека **re** и **matplotlib** (смотри *requirements.txt*)

## Работа с ссылками ftp

При запуске скрипта код автоматически считывает файл *ref.txt*, выбирает из него все **УНИКАЛЬНЫЕ** ссылки ftp и сохраняет их в файл *ftps.txt*. Ссылки сортированы.

## Работа с текстом

При запуске скрипта код автоматически считывает файл *2430AD.txt*. Производится подсчет следующих показателей:

1.  Всех цифр. Выводит на печать список.

2.  Всех слов, содержащих букву а. Выводит на печать список.

3.  Всех воскрицательных предложений. Выводит на печать список.

4.  Всех уникальных слов. Выводит гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте. То есть по оси x идёт длина слова. По оси y идёт доля слов с такой длиной среди уникальных слов, найденных в тексте. При этом слова the и The считаются одним словом, то есть регистр не важен

## Функции

**translate** - принимает на вход текст. Выводит текст с переводом на кирпичный язык. Вставленные слоги для визуального удобства сделаны заглавными. Например:

```{python}
In[]: translate("молоко железо привет")
Out[]:моКОлоКОкоКО жеКЕлеКЕзоКО приКИвеКЕт
```

**sentence_finder** - принимает на вход текст и число. Функция возвращает список кортежей, каждый из которых содержит отдельные слова из найденных предложений. Например:

```{python}
In[]:find_n_words_sentences("Здесь три слова. Здесь тоже три.", 3) 
Out[]:[("Здесь", "три", "слова"), ("Здесь", "тоже", "три")]
```
