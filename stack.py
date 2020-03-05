from LinkedList import SingleLinkedList


class Stack:
    def __init__(self):
        self.mylist = SingleLinkedList

    def push_stack(self,data):
        SingleLinkedList.add_head(data)
        return data

    def pop_stack(self):
        return SingleLinkedList.remove_head()
