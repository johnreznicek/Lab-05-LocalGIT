from Employee import Employee

class Payroll():
  def __init__(self):
    self.emp = []

  def __repr__(self):
    return str(self.emp)
  
  def addEmp(self, e):
    self.emp.append(e)

  def total(self):
    """Calculates and returns the total payroll for all employees."""
    total_pay = 0
    for employee in self.emp:
      # Assuming Employee class has a method to get employee pay (e.get_pay())
      total_pay += employee.get_pay()
    return total_pay