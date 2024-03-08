# TestTasks_LestaGamesIntern

В данном репозитории ответы на тестовые задания на стажировку Intern Programmer (Game Logic), предоставленную компанией Lesta Games

## Задание 1

**Условие:**

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Пример: 

```python
def isEven(value):
    return value % 2 == 0
```
<br />

**Решение:**

```python
def isEven(value):
    return value & 1 == 0
```

Суть данной функции заключается в проверке последнего бита числа в его двоичном представлении.
Если бит равен 0, то число чётное. Если же бит равен 1 (остальных целых значений в двоичном представлении
не существует), то число нечётное.

Плюсом этого решения является скорость, так как побитовое умножение в контексте задачи занимает меньше времени,
чем циклическое деление числа, пока оно не станет меньше делителя. Однако во время тестирования компилятор
мгновенно решил задачу для обоих алгоритмов даже на больших числах.

Очевидных минусов решения нет, разве что это решение не самое очевидное, потому что в ход идёт двоичное
представление числа, но это больше придирка, нежели минус.

Исходный код лежит в папке с [заданием 1](https://github.com/PKS339057/TestTasks_LestaGamesIntern/tree/main/Tasks/Task%201).


## Задание 2

**Условие:**

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.

Оценивается:

1. Полнота и качество реализации
2. Оформление кода
3. Наличие сравнения и пояснения по быстродействию
<br />

**Решение:**

Дисклеймер: за основу реализации циклического буфера FIFO было взято задание 622 из платформы LeetCode.
Обращу внимание, что задание пригодилось только для того, чтобы выбрать методы, которые будут реализованы в
структуре данных. Вся логика прописана мной, следовательно, код не заимствован.

В первом классе циклический буфер реализован с помощью массива. Код для реализации класса лежит в файле
[array_circular_fifo.py](https://github.com/PKS339057/TestTasks_LestaGamesIntern/tree/main/Tasks/Task%202/array_circular_fifo.py)

Во втором классе циклический буфер реализован с помощью односвязного списка. Код для реализации класса лежит в файле
[linked_list_circular_fifo.py](https://github.com/PKS339057/TestTasks_LestaGamesIntern/tree/main/Tasks/Task%202/linked_list_circular_fifo.py)

Ссылка на исходный код:


## Задание 3

**Условие:**

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

<br />

**Решение:**

Ссылка на исходный код:
