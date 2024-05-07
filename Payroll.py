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
      total_pay += employee.get_pay()
    return total_pay

  def employeePay(self, lastName):
    """Returns the pay of the employee with the matching last name, or None if not found."""
    for employee in self.emp:
      if employee.getLastName() == lastName:
        return employee.getPay()
    return None  # Or an informative message