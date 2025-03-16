"""
Design Dynamic Array (Resizable Array)

Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

    DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    int get(int i) will return the element at index i. Assume that index i is valid.
    void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    void pushback(int n) will push the element n to the end of the array.
    int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    void resize() will double the capacity of the array.
    int getSize() will return the number of elements in the array.
    int getCapacity() will return the capacity of the array.

If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:
    ```
    Input:
    ["Array", 1, "getSize", "getCapacity"]

    Output:
    [null, 0, 1]
    ```

Example 2:
    ```
    Input:
    ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

    Output:
    [null, null, 1, null, 2]
    ```

Input:
    ```
    ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

    Output:
    [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
    ```
"""


class DynamicArray:
    def __init__(self, capacity: int):
        self.data = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        if self.length > i:
            return self.data[i]
        else:
            return -1

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.data[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.data[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.data[i]

        self.data = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
