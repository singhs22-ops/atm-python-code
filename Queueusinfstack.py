
class Queue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def Enqueue(self,x):

        while (len(self.s1)!=0):
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while(len(self.s2)!=0):
            self.s1.append(self.s2[-1])
            self.s2.pop()


    def Dequeue(self):
        if(len(self.s1)==0):
            print("Empty queue")

        x=self.s1[-1]
        self.s1.pop()
        print(x)


if __name__ == '__main__':
    q = Queue()
    q.Enqueue(33)
    q.Enqueue(28)
    q.Enqueue(89)
    q.Enqueue(90)
    q.Enqueue(87)
    q.Enqueue(90)
    q.Enqueue(33)
    q.Enqueue(65)

    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()