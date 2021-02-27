import re

def numeric(f,equation,s):
    if '+' in equation:
        x = int(f)+int(s)
    elif '-' in equation:
        x = int(f)-int(s)
    return str(x)

def falseCheck_operator(operator):
  if '/' in operator or '*' in operator:
    return False
  else:
    return True

def digitLength(number):
  counter = 1
  while(number>=10):
    counter +=1
    number = int(round(number/10))  
  return counter

def verticalCalculation(firstnum, mathoperator, secondnum,sh):
  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''
  for i in range(len(firstnum)):
    maxi = max(digitLength(int(firstnum[i])),digitLength(int(secondnum[i])))+2
    first_line = first_line + firstnum[i].rjust(maxi) + " "*4
    second_line = second_line + mathoperator[i] + secondnum[i].rjust(maxi-1) + " "*4
    third_line = third_line + "-"*maxi +" "*4
    fourth_line = fourth_line + numeric(firstnum[i],mathoperator[i],secondnum[i]).rjust(maxi)+ " "*4
  if sh == True:
    text = "\n".join([first_line[:-4],second_line[:-4],third_line[:-4],fourth_line[:-4]])
  else:
    text = "\n".join([first_line[:-4],second_line[:-4],third_line[:-4]])
  return text
  
def arithmetic_arranger(problems,show=False):
    num = []
    op = []
    first = []
    second = []
    new_op = []
    msg =''
    #print(len(problems))
    if len(problems)<=5:
      #take the numbers and operators
      for i in problems:
        num.append(re.findall('[0-9]+', i))
        op.append(re.findall('[+-/]+', i))
        y = re.findall('[a-z]',i)
        if y :
          msg = "Error: Numbers must only contain digits."
          break
      
      if not msg :
      #split first numbers, operators, second numbers
        for i in range(len(num)):
          for j in range(len(num[i])):
            if j%2 == 0 :
              first.append(num[i][j])
            else:
              second.append(num[i][j])
          new_op.append(op[i][0])

        #check the operators  
        operator = falseCheck_operator(new_op)
        if operator == True:
          #check if more than 5 digit
          for i in range(len(first)):
            if int(first[i]) > 9999 or int(second[i]) > 9999:
              msg = "Error: Numbers cannot be more than four digits."
              
          if not msg:
            #create vertical calculation string
            arranged_problems = verticalCalculation(first,new_op,second,show)
        else:
          msg = "Error: Operator must be '+' or '-'."
    else:
      msg = "Error: Too many problems."

    if msg:
      return msg
    else:
      return arranged_problems