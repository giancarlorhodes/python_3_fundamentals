# exception handling
# _some_dict = {'LOL': 'laugh out loud',
#               'IDK': 'I don\'t know',
#               'TBH': 'To be honest'}
#
#
#
# try:
#     _def = _some_dict['BTW']
# except:
#     print("The key does not exist.")
# finally:
#     print("will execute whether there is error or not. Good place to do clean up ...")

# print("code continues ...")



with open('acronyms.txt') as file:
    # do my file operations here
    #_results_entire_file = file.read()

    #print(_results_entire_file)
    
    _results_line_by_line = file.readlines() # returns a list of strings

    for _line in _results_line_by_line:
        print(_line)
    
    file.close()

_new_acro = input("What acronym do you want to add?\n")
_new_def = input("What is the new definition?\n")

with open('acronyms.txt', 'a') as file:
    file.write(_new_acro + " - " + _new_def + "\n") 
    file.close()


