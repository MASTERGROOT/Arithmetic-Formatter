
def cal_arithmetic_arranger(Question,show_ans = True):
    if len(Question) > 5:
        return "Error: Too many problems."

    First_operand = []
    Second_operand = []
    operator = []

    for problem in Question:
        pieces = problem.split()
        First_operand.append(pieces[0])
        Second_operand.append(pieces[2])
        operator.append(pieces[1])
    
    if "*" in operator or  "/" in operator:
        return "Error: Operator must be '+' or '-'."
    
    numerical_check = all(x.isdigit() for x in First_operand and Second_operand)
    if numerical_check == False:
        return "Error: Numbers must only contain digits."
    
    for number in zip(First_operand,Second_operand):
        if len(number[0]) > 4 or len(number[1]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []
    
    for i in range(len(First_operand)):
        if len(First_operand[i]) > len(Second_operand[i]):
            first_line.append("  " + First_operand[i])
        else:
            first_line.append(" " * (len(Second_operand[i]) - len(First_operand[i])+ 2) + First_operand[i])
        
    for i in range(len(Second_operand)):
        if len(Second_operand[i]) > len(First_operand[i]) :
            second_line.append(operator[i] + " " + Second_operand[i])
        else:
            second_line.append(operator[i] + " " * (len(First_operand[i]) - len(Second_operand[i])+ 1) + Second_operand[i])
    
    for i in range(len(First_operand)):
        length = max(len(First_operand[i]), len(Second_operand[i])) + 2
        third_line.append("-" * length)
    # return first_line, second_line, third_line
    if show_ans == True:
        for i in range(len(Question)):
            if operator[i] == "+":
                result = str(int(First_operand[i]) + int(Second_operand[i]))
            
            elif operator[i] == "-":
                result = str(int(First_operand[i]) - int(Second_operand[i]))
            
            if len(result) > max(len(First_operand[i]), len(Second_operand[i])):
                fourth_line.append(" " + result)
            else:
                fourth_line.append(" " * (max(len(First_operand[i]), len(Second_operand[i])) - len(result) + 2) + result)
        ans = " ".join(first_line) + "\n" + " ".join(second_line) + "\n" +" ".join(third_line) + "\n" + " ".join(fourth_line) 
        return ans
    else:
        ans = " ".join(first_line) + "\n" + " ".join(second_line) + "\n" +" ".join(third_line)
        return ans
