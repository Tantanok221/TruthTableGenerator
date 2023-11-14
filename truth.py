import ttg
import prettytable

def generateHTML(table,name):
  table.format = True
  newTable = table.get_html_string()
  # replace all  "or" with "+" and "and" with "*"
  newTable = newTable.replace("or", "+")
  newTable = newTable.replace("and", "*")
  # replace all the newTable "~" to "'" at the same time move it to the right
  newTable = newTable.replace("~", "'")
  newTable = newTable.replace("'a", "a'")
  newTable = newTable.replace("'b", "b'")
  newTable = newTable.replace("'c", "c'")
  newTable = newTable.replace("'d", "d'")
  # save the html file
  with open(name + '.html', 'w') as f:
      f.write(newTable)


# Generate a html file with truth table based on teacher requirement.

threeOriTable = ttg.Truths(["a", "b", "c"], 
["~a",
"~b",
"~c",
"~a and ~c", # First expressiom
"~a and ~b", # Second Expression
"b or ~c", # Third expression (nested without bar)
"~(b or ~c)",  # Third expression (nested with bar)
"a and ~(b or ~c)", # Third expression (without nested)
"~(b and ~(b or ~c))", # Forth expression (without nested)
"(~a and ~c) or ~b",#Answer

]
, ascending= True
).as_prettytable()

threeNewTable = ttg.Truths(["a", "b", "c"], 
["~a",
"~b",
"~c",
"~a and ~c", # First expressiom
"(~a and ~c) or ~b"

]
, ascending= True
).as_prettytable()

fourOriTable = ttg.Truths(["a", "b", "c", "d"],
[
  "~b",
  "~c",
  "~d",
  "a and ~b and c", # first expression
  "a and ~b", # second expression
  "~b and c", # third expression
  "~b and ~c and ~d", # forth expression
  "a and c and ~d",# fifth expression without nested
  "~(a and c and ~d)", # fifth expression with nested
  "(a and ~b and c) or (a and ~b) or (~b and c) or (~b and ~c and ~d) or ~(a and c and ~d)", # answer
], ascending= True).as_prettytable()

fourNewTable = ttg.Truths(["a", "b", "c", "d"],[
  "~a",
  "~b",
  "~c",
  "~a or ~b or ~c or d"
  ],ascending = True).as_prettytable()



