#!/usr/bin/python
import words,stack_as
import sys, re
def main():
        
    whitespace = re.compile(r"[ \t\n]+")
    number = re.compile(r"-?[0-9]+")
    if(len(sys.argv) != 3):
        print "Usage: ./compiler.py [forth] [assembly]"
        sys.exit(-1)
    lines = open(sys.argv[1],"r").read()
    outfile = open(sys.argv[2],"w")
    tokens = whitespace.split(lines)
    tokens_iter = iter(tokens)
    ifthen_count = 0
    asm_text = "nop\nnop\n"
    for token in tokens_iter:
    
        token.strip()
        if token:
            if number.match(token):
                asm_text += "push " + token + "\n"
            elif token in words.core_words:
                asm_text += words.core_words[token] + "\n"
            elif token in words.words:
                asm_text += "call "+token+ "\n"
            elif token in words.other_words:
                print "other words " + token
                asm_text += "call "+token+ "\n"
                words.copy_word(token)
            elif token == "IF":
                print token
                asm_text += "cjump then"+str(ifthen_count)+"\n"
            elif token == "THEN":
                asm_text += "then"+str(ifthen_count) + ":\n"
                ifthen_count += 1
            elif token == ":":
                new_word = []
                for w_token in tokens_iter:
                    print w_token
                    if w_token is ";":
                        break
                    else:
                        new_word.append(w_token)
                words.add_word(new_word)
            elif token == "(":
                for w_token in tokens_iter:
                    if w_token is ")":
                        break
            elif token == "\\":
                 for w_token in tokens_iter:
                    if w_token is "\n":
                        break
        
    asm_text +="jump end\n"
    asm_text +=words.wordlines
    asm_text +="end: nop\n"
    print asm_text
    out_lines = asm_text.split("\n")
    arr = stack_as.main(out_lines)
    outfile.write(bytearray(arr))
