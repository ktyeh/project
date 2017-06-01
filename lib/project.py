# -*-coding=utf8-*-
'''
Example Docstring
'''
class Project:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print 'My name is "%s"' % self.name
    
    @property
    def name_size(self):
        return len(self.name)
