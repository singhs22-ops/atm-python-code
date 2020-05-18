

def Node(self,dataval= None):
    self.dataval =dataval
    self.next = None
    return

class llist:
    def __init__(self):
        self.headval = None

    def insert_head(self,dataval= None):
        new_node = Node(dataval)
        new_node.next = head_val
        head_val = new_node

    def insert_back(self, data):
        new_node = Node(data)
        head1 = head

        if head1.next != None:
            head1 = head.next

        head1.next = new_node


def listprint(head):
        printval = head
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

head = llist()
head.insert_head(6)
listprint(head)
   # head.insert_head(3)
    #head.insert_back(6)
