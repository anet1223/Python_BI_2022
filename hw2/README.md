# fastq_filtrator.py.

## Описание

Программа содержит функцию **main**, которая принимает на вход несжатый fastq файл и фильтрует в нем риды по качеству, длине или содержанию GC. Результат можно сохранить в двух новых файлах.

## Аргументы

**input_fastq** - путь к файлу, который подаётся на вход программе. где лежит fastq файл. Если их в папке несколько, берется первый. Для Windows путь имеет вид `“C:\\xyz\\Documents\\My all docs”`. Для Linux/Unix путь имеет вид `“/Documents/Myfolder”`.

**output_file_prefix** - префикс названия файла, в который будет записан результат. К префиксу прибавляется *"_passed.fastq"* для файла с ридами, прошедшими фильтрацию и *"_failed.fastq"* для файлов с отфильтрованными ридами (только если аргумент save_filtered равен True). Например, `output_file_prefix = 'new'`. Результат записывается в ту же папку, где лежал исходный fastq.

**gc_bounds** - интервал GC состава (в процентах) для фильтрации (по умолчанию равен (0, 100), т. е. все риды сохраняются). Если в аргумент передать одно число, то считается, что это верхняя граница. Примеры: `gc_bounds = (20, 80)` - сохраняются только риды с GC составом от 20 до 80% включительно, `gc_bounds = 44.4` - сохраняем риды с GC составом меньше или равно 44.4%.

**length_bounds** - интервал длины для фильтрации, по-умолчанию равен (0, 2\*\*32). Указанные границы включаются.

**quality_threshold** - пороговое значение среднего качества рида для фильтрации, по-умолчанию равно 0 (шкала phred33). Риды со средним качеством по всем нуклеотидам ниже порогового отбрасываются

**save_filtered** - сохранять ли отфильтрованные риды, по-умолчанию равен False.
