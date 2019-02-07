from Linked-List import Node

class LinkedList(object):

  def __init__(self, r=None):
    self.root = r
    self.size = 0
    
  def get_size(self):
    return self.size
    
  def add(self, d):
    new = Node(d, self.root)
    self.root = new
    self.size += 1
    
  def remove(self, d):
    this = self.root
    prev = None
    
    while(this):
      if this.get_data() == d:
        if prev:
          prev.set_next(this.get_next())
        else:
          self.root = this.get_next()
        self.size -= 1
        return True
      else:
        prev = this
        this = this.get_next()
    return False
    
  def find(self, d):
    this = self.root
    while(this):
      if(this.get_data()==d):
        return d
      elif(this.get_next()==None):
        return False
      else:
        this = this.get_next()
