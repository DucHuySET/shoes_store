
### Create Singleton app controller
class AppController(object):
  user = None
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(AppController, cls).__new__(cls)
    return cls.instance