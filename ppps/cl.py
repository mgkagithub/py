class parent:
  def __init__(self): 
    self.height = '6 foot'
    self.eye = 'green'  
  skin = 'white'
class child(parent):
  def __init__(self,height):
    super().__init__(height)
obj = child('6foot')
print(obj.height)