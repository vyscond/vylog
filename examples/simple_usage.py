from whysper import Whysper

class Foo :

    def __init__( self ):
        
        self.log = Whysper( self )

        self.log.show('[Foo has been instantiated]')

    def boo( self ):

        self.log.show('[calling boo function]')

# ---

f = Foo()

f.boo()

