import re
number = re.compile(r"-?[0-9]+")
whitespace = re.compile(r"[ \t\n]+")
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
    ">R":"rpush",
    "R>":"rpop",
    "r@":"rcp",
    "R@":"rcp",
    "DO":"call 0\n",
    "LOOP":"push 1\n add\n dup\n rot\n dup\n rot\n eq\n neg\n cjump 9\n drop\n swap\n rcp\n rpush\n ret",
    "0=":"push 0\neq",
    "0<":"push 0\nlt",
    "0>":"push 0\ngt",
    "AND":"and",
    "OR":"or",
    "XOR":"xor",
    "LSHIFT":"lshift",
    "RSHIFT":"rshift",
    "<<":"lshift",
    ">>":"rshift",
    "*":"mul",
    "@":"fetch",
    "!":"store",
}
other_words = {
    "NIP": "NIP SWAP DROP",
    "NROT":"NROT ROT ROT",
    "TUCK":"TUCK DUP NROT",
    "OVER":"OVER SWAP TUCK",
    "+!":"+! DUP @ ROT + SWAP !",#val addr +!
    "NEGATE":"NEGATE 0 SWAP -",
    "1+":"1+ 1 +",
    "1-":"1- 1 -",
    "?DUP":"?DUP DUP IF DUP THEN",
    
}
words = [

]

wordlines = ""
ifthen_count = 0
def copy_word(token):
    add_word(whitespace.split(other_words[token]))

def add_word(tokens):
    print tokens
    global ifthen_count
    global wordlines
    word = tokens.pop(0)
    words.append(word)
    
    wordlines += word + ":\n"
    for token in tokens:
        needs_ret = True
        if number.match(token):
            wordlines += "push " + token + "\n"
        elif token in core_words:
            wordlines += core_words[token] + "\n"
        elif token in words:
            wordlines += "call "+token+ "\n"
        elif token in other_words:
            wordlines += "call "+token+ "\nret\n"
            needs_ret = False
            add_word(whitespace.split(other_words[token]))
        elif token == "IF":
            wordlines += "cjump thenw"+str(ifthen_count)+"\n"
        elif token == "THEN":
            wordlines += "thenw"+str(ifthen_count) + ":\n"
            ifthen_count += 1
    if needs_ret:
        wordlines += "ret\n"
            
        
