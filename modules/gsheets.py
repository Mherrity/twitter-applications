import pygsheets


class WorkSheet:
  def __init__(self, config_path, spreadsheet_name):
    self.ws = self.get_worksheet(config_path, spreadsheet_name)
    self.ProfileRange = 'C2:C'

  
  def userExists(self, user):
    for cell in self.ws.range(self.ProfileRange):
      val = cell[0].value
      if val == '':
        return (False, cell[0].address)
      if val == user['profile']:
        return (True,'')
  
  def publish_user(self,User,address):
    values = [User['user_id'], User['name'], User['profile'], User['thread']]
    self.ws.update_row(address.row,values)
  
  def proccess_user(self,user):
    exists,address = self.userExists(user)
    if not exists:
      self.publish_user(user,address)
      return True
    else:
      return False
    
  def get_worksheet(self,config_file,spreadsheet_name):
      gc = pygsheets.authorize(service_file=config_file)
      sh = gc.open(spreadsheet_name)
      return sh[0]




 