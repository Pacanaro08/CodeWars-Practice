# def eval_parentheses(s):
#     format_string(s)
    
# def format_string(s):
#     fs = ''
#     ss = ''
#     i = len(s)
#     while i > 0:
#         for ps in s:
#             if fs == '':
#                 fs = ps
#             elif ss == '':
#                 ss = ps
#                 fullCalc = calc(fs, ss)
#                 s = s[:0] + s[2:]
#                 break
#         format_string(s)
#     print(fullCalc)
    
# def calc(fs, ss):
    
#     if fs == '(' and ss == ')':
        
#         fullCalc = fullCalc + '1'
#     elif fs == '(' and ss == '(':
#         fullCalc = fullCalc + '2*'

#     return fullCalc
# fullCalc = ''


# def eval_parentheses(s):
#     for ps in s:
        
#     return calcResult


# eval_parentheses("()()")
