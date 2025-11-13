def fun(x):
    result = ''
    for i in x[:-1]:
        result +=  str(i) + ","
    result += "and " + x[-1]
    print(result)
    
spam = ['apples','bananas','tofu','cats']
fun(spam)
