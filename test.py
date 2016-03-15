import whysper

class Foo(object):
    def __init__(self):
        self.log = whysper.Whysper(self)
        self.log('a new class has being instantiated')

    def boo(self):
        self.log('boo has being called')

foo = Foo()
foo.boo()
