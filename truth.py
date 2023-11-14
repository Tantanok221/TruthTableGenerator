import ttg

def generateHTML(table,name):
  oldTable = table.as_prettytable()
  oldTable.format = True
  newTable = oldTable.get_html_string()
  # replace all  "or" with "+" and "and" with "*"
  newTable = newTable.replace("or", "+")
  newTable = newTable.replace("and", "*")
  # replace all the newTable "~" to "'" at the same time move it to the right
  newTable = newTable.replace("~", "'")
  newTable = newTable.replace("'a", "a'")
  newTable = newTable.replace("'b", "b'")
  newTable = newTable.replace("'c", "c'")
  newTable = newTable.replace("'d", "d'")
  # create a folder call outdir
  # write the newTable to a html file
  outdir = "outdir"
  outfile = open(outdir + "/" + name + ".html", "w")
  outfile.write(newTable)
  outfile.close()
  
  
  
  
  
def generateTable(var,condition):
  table = ttg.Truths(var,condition,ascending = True)
  return table

# Generate a html file with truth table based on teacher requirement.

fourOriTable = generateTable(["a", "b", "c", "d"],
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
])

generateHTML(fourOriTable,"fourOriTable")

