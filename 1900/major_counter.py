major_storage = {}

major = input("Enter major of student (X to exit): ")

while major.upper() != 'X':
  
  if major in major_storage:
    major_storage[major] += 1
  else:
    major_storage[major] = 1

  major = input("Enter major of student (X to exit): ")

if major.upper() == 'X':
  for key, val in major_storage.items():
    print(key, '-', val)

major_code = {
  'COMP': ['compsci', 'comp sci', 'computer sci', 'computer science'],
  'CMPE': ['compeng', 'comp eng', 'computer eng', 'computer engineering'],
  'EE': ['eleceng', 'elec eng', 'elec engineering', 'electrical engineering'],
  'MATH': ['mathsci', 'math sci', 'mathematical sci', 'mathematical sciences', 'mathematics']
}

def get_major_code(major):
  ret_val = major.upper()
  for code, variants in major_code.items():
    if major.lower() in variants:
      ret_val = code
      break
  
  return ret_val

major_code = {
  'COMP': ['compsci', 'comp sci', 'computer sci', 'computer science'],
  'CMPE': ['compeng', 'comp eng', 'computer eng', 'computer engineering'],
  'EE': ['eleceng', 'elec eng', 'elec engineering', 'electrical engineering'],
  'MATH': ['mathsci', 'math sci', 'mathematical sci', 'mathematical sciences', 'mathematics']
}

def get_major_code(major):
  ret_val = major.upper()
  for code, variants in major_code.items():
    if major.lower() in variants:
      ret_val = code
      break
  
  return ret_val

major_storage = {}

major = input("Enter major of student (X to exit): ")

while major.upper() != 'X':
  major = get_major_code(major)
  if major in major_storage:
    major_storage[major] += 1
  else:
    major_storage[major] = 1
  major = input("Enter major of student (X to exit): ")

if major.upper() == 'X':
  for key, val in major_storage.items():
    print('Summary of data entered:')
    print(key, '-', val)







