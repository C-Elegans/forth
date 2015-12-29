import re
number = re.compile(r"-?[0-9]+")
core_words = {
    "+" : "add",
    "-" : "sub",
    "." : "out",
    "DUP": "dup",
    "DROP": "drop",
    "SWAP": "swap",
    "ROT": "rot",
    "<": "lt",
    "=": "eq",
    ">": "gt",
    "INVERT": "neg",
    ">r":"rpush",
    "r>":"rpop",
    "r@":"rcp",
}
words = [

]
wordlines = ""
ifthen_count = 0
def add_word(tokens, outfile):
    global ifthen_count
    global wordlines
    word = tokens.pop(0)
    words.append(word)
    
    wordlines += word + ":\n"
    for token in tokens:
        if number.match(token):
            wordlines += "push " + token + "\n"
        elif token in core_words:
            wordlines += core_words[token] + "\n"
        elif token in words:
            wordlines += "call "+token+ "\n"
        elif token == "IF":
            wordlines += "cjump thenw"+str(ifthen_count)+"\n"
        elif token == "THEN":
            wordlines += "thenw"+str(ifthen_count) + ":\n"
            ifthen_count += 1
    wordlines += "ret\n"
            
        
