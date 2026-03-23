# 1
class RangeIterator:

    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.end:
                raise StopIteration
            value = self.current
            self.current += self.step
            return value
        elif self.step < 0:
            if self.current <= self.end:
                raise StopIteration
            value = self.current
            self.current += self.step
            return value
        else:
            return "Нулевой шаг"

itter = RangeIterator(50, 30, -2)
for i in itter:
    print(i)

print(next(itter))

# 2
def gen_fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for i in gen_fib(20):
    print(i, end=' ')

# 3
class LogReader:


    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            line = self.text[self.index]
            self.index += 1
            if line.strip():
                return line
        raise StopIteration


str_1, str_2, str_3, str_4 = input(), input(), input(), input()
text = [str_1, str_2, str_3, str_4]
reader = LogReader(text)
for line in reader:
    print(line)

# 4
def flatten(iterable):
    for elem in iterable:
        if isinstance(elem, list):
            for item in flatten(elem):
                yield item
        else:
            yield elem
gen_fun = flatten([1, [2, 3], [[4], 5], 6])
for i in gen_fun:
    print(i, end=' ')