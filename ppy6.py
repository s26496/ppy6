
#Tylko pierwsza część (zad1)
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        current = self.head
        out = []
        while current:
            out.append(str(current.data))
            current = current.nextE
        return ' -> '.join(out)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        prev = None
        while current:
            if current.data == e:
                if prev:
                    prev.nextE = current.nextE
                else:
                    self.head = current.nextE
                self.size -= 1
                return
            prev = current
            current = current.nextE
        return None

    def append(self, e, func=None):
        element = Element(e)
        if not self.head:
            self.head = element
            self.tail = element
        else:
            if func:
                current = self.head
                prev = None
                while current:
                    if func(current.data, e):
                        element.nextE = current
                        if prev:
                            prev.nextE = element
                        else:
                            self.head = element
                        break
                    prev = current
                    current = current.nextE
                if current is None:
                    prev.nextE = element
                    self.tail = element
            else:
                if e >= self.tail.data:
                    self.tail.nextE = element
                    self.tail = element
                else:
                    current = self.head
                    prev = None
                    while current:
                        if current.data >= e:
                            element.nextE = current
                            if prev:
                                prev.nextE = element
                            else:
                                self.head = element
                            break
                        prev = current
                        current = current.nextE
        self.size += 1
