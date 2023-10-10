
statement = ['Thirty', 'Days', 'Of', 'Python']
statement_2 = ['Coding', 'For' , 'All']
concat_statement = ' '.join(statement)
concat_statement_2 = ' '.join(statement_2)
print(concat_statement_2)

company = concat_statement_2
company_len = len(company)
block_case = company.upper()
small_case = company.lower()
capitalize_comp = company.capitalize()
title_comp = company.title()
swap_comp = company.swapcase()
slice_comp = company[0:6]
state = "Coding"

if(company.__contains__(state)):
    print(f"{state} is avalable in the statement")
else:
    print(f"{state} not available in the statement")

company_3 = company.replace("Coding", "Python")
company_4 = company_3.replace("All", "Everyone")
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech_split = tech.split(",")

split_statement = company.split(" ")
com_index =company[0]
com_last_index =company[-1]
com_tenth_index = company[10] #the index at the 10th value is space
# lets create an acronym from the "python for all"

# step 1 
#  split the statement into individual elements

# step 2 Iterate through each words to get the position of the first letter in each words index


acronym = []
acronym_2 = []
words = company_3.split()

for word in words:
    word = word[0]
    acronym.append(word)
print(acronym)


words_2 = concat_statement_2.split()

for word in words_2:
    acronym_2 += word[0]
print(acronym_2)