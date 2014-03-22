class Cell(object):
    
    def __init__(self, state=False):
        self._alive = state
        
    @property
    def alive(self):
        return self._alive
        
    @alive.setter
    def alive(self, state):
        self._alive = state
        
    def __str__(self):
        return '''{0}'''.format(int(self.alive))        
        
    def __repr__(self):
        return '''{0}'''.format(int(self.alive))                  