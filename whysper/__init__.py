__author__ = 'Ramon Moraes'
__version__ = '0.1.0'
__license__ = 'MIT'

import os
from datetime import datetime

class Stream(object):
    def show(self, content):
        raise NotImplemented

class OutputStream(Stream):
    def show(self, content):
        print(content)

class FileStream(Stream):
    pass

class Whysper(object):

    APPEND = 'a'
    WRITE  = 'w'

    def __init__( self , class_reference ):

        self.header = '{} - {}'.format(
            self.gen_timestamp(),
            str(class_reference.__class__.__name__)
        )

        self.log_lines = []
    
    def __call__(self, msg):
        self.show(msg)

    def dump_log_to(self, path, mode):
        with open(os.path.join(path, 'log.txt'), 'w') as f:
            f.write('\n'.join(self.log_lines))

    def show( self , msg ):
        msg = '{} -> {}'.format(self.header, msg)
        self.log_lines.append(msg)
        print(msg)

    def gen_timestamp(self, strf='%Y/%m/%d - %H:%m:%s'):
        date = datetime.today()
        return date.strftime(strf)

