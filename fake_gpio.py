class FakeAttr(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        arguments = [str(a) for a in args]
        arguments.extend('{}={}'.format(n,str(v)) for n,v in kwargs.items())
        
        print('[GPIO Call] {}({})'.format(self.name, ','.join(arguments)))

class FakeGPIO(object):
    
    def __getattr__(self, name):
        return FakeAttr(name)