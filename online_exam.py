#online exam
from pywebio.input import *
from pywebio.output import *
def exam():
    c=0 #count for save score

    name=input("Please enter your name",type="text")

    q1=radio("what is the maximum possible length of an identifier?",['16','32','64','None of these'])
    if q1=='None of these':
        c+=1

    q2=radio("who developed python languager?",['Zim Den','Guido van Rossum','Niene Storm','Wick van Rossum'])
    if q2=='Guido van Rossum':
        c+=1

    q3=radio("in which language python written?",['English','PHP','C','All of these'])
    if q3=='c':
        c+=1

    q4=radio("which of the following is the correct extension of the python file?",['.py','.python','.p','None of these'])
    if q4=='.py':
        c+=1

    q5=radio("what do we use to define a block of code in python language?",['Key','Brackets','Indentation','None of these'])
    if q5=='Indentation':
        c+=1
    q6=radio("which character is used in python to make a single line comment?",['/','//','#','!'])
    if q6=='#':
        c+=1
    q7=radio("what is the method inside the class in python language?",['Object','Function','Attribute','Argument'])
    if q7=='Function':
        c+=1
    q8=radio("which of the following words cannot be a variable in python languager?",['_val','val','try','_try_'])
    if q8=='try':
        c+=1
    q9=radio("which of the following is not a keyword in python language?",['val','raise','try','with'])
    if q9=='val':
        c+=1
    q10=radio("which of the following has the highest precedence in the expression?",['Division','Substraction','Power','Parentheses'])
    if q10=='Parentheses':
        c+=1
    
    #Checks For Pass Fail
    if c>=6:
        put_text(name +",your score is"+ str(c))
        style(put_text("result : Passed"),"color:green")
    else:
        put_text(name +",your score is"+ str(c))
        style(put_text("result : Failed"),"color:red")
    put_text("Thank you for your participation")
exam()









