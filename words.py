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
}
words = [

]
wordlines = ""
def add_word(tokens, outfile):
    
    global wordlines
    word = tokens.pop(0)
    words.append(word)
    print word + ": " + str(tokens) 
    
    wordlines += word + ":\n"
    for token in tokens:
        if number.match(token):
            wordlines += "push " + token + "\n"
        elif token in core_words:
            wordlines += core_words[token] + "\n"
        elif token in words:
            wordlines += "call "+token+ "\n"
    wordlines += "ret\n"
            
        
