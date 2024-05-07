from Employee import Employee

class Payroll():
  def __init__(self):
    self.emp = []

  def __repr__(self):
    return str(self.emp)
  
  def addEmp(self, e):
    self.emp.append(e)

  def total(self):
    total_pay = 0
    for employee in self.emp:
      # Assuming Employee class has a method to get employee pay (e.get_pay())
      total_pay += employee.get_pay()
    return total_pay
  def sort(self):
    for i in range(len(self.emp)):
      # Find the index of the employee with the maximum pay in the unsorted part
      max_index = i
      for j in range(i + 1, len(self.emp)):
        if self.emp[j].get_pay() > self.emp[max_index].get_pay():
          max_index = j
      # Swap the employee with the maximum pay with the current element
      self.emp[i], self.emp[max_index] = self.emp[max_index], self.emp[i]