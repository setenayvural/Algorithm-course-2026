class Node:
    def __init__(self,content):
        self.content=content
        self.next=None
class linked_list:
    def __init__(self):
        self.front=None
        self.rear=None
    def add_front(self,new):
        if self.front==None:
            self.front=Node(new)
            self.rear=Node(new)
        else:
            Node(new).next=self.front
            self.front=Node(new)
    def add_rear(self,new):
        if self.rear==None:
            self.front=Node(new)
            self.rear=Node(new)
        else:
            self.rear.next=Node(new)
            self.rear=Node(new)
    def count_words(self):
        current=self.front
        while current!=None:
            print("Word count: ", len(current.content.split()))
            current = current.next

my_list = linked_list()
my_list.add_rear("No description, website or topics provided.")
my_list.count_words()
