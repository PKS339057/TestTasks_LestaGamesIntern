from ICircularFIFO import ICircularFIFO
from array_circular_fifo import ArrayCircularFIFO
from linked_list_circular_fifo import LinkedListCircularFIFO


def test(c_fifo: ICircularFIFO) -> None:
    print(f"Тест для класса {type(c_fifo).__name__}\n")
    print("Проверка частично заполненной очереди")
    for el in range(3):
        c_fifo.enqueue(el)
    __print_result(c_fifo)
    for _ in range(2):
        c_fifo.dequeue()
    __print_result(c_fifo)
    for el in range(3, 5):
        c_fifo.enqueue(el)
    __print_result(c_fifo)
    __print_line()
    print("Проверка полной очереди")
    for el in range(2):
        c_fifo.enqueue(el)
    __print_result(c_fifo)
    print(f"Результат заполнения полной очереди: {c_fifo.enqueue(5)}")
    __print_line()
    print("Проверка пустой очереди")
    for _ in range(c_fifo.size):
        c_fifo.dequeue()
    __print_result(c_fifo)  # Результат равен -1 по условию из задания LeetCode
    print(f"Результат удаления элемента из пустой очереди: {c_fifo.dequeue()}")


def __print_result(c_fifo: ICircularFIFO):
    print("Текущее состояние: ", end="")
    c_fifo.print_buffer()


def __print_line():
    print("-" * 20)


if __name__ == "__main__":
    arr_fifo = ArrayCircularFIFO(5)
    ll_fifo = LinkedListCircularFIFO(5)
    test(arr_fifo)
    print("\n")
    test(ll_fifo)
