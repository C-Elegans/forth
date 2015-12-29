#!/usr/bin/python
import words
import sys, re

whitespace = re.compile(r"[ \t\n]+")
number = re.compile(r"-?[0-9]+")
if(len(sys.argv) != 3):
    print "Usage: ./compiler.py [forth] [assembly]"
lines = open(sys.argv[1],"r").read()
outfile = open(sys.argv[2],"w")
tokens = whitespace.split(lines)
tokens_iter = iter(tokens)
ifthen_count = 0
for token in tokens_iter:
    
    token.strip()
    if token:
        if number.match(token):
            outfile.write("push " + token + "\n")
        elif token in words.core_words:
            outfile.write(words.core_words[token] + "\n")
        elif token in words.words:
            outfile.write("call "+token+ "\n")
        elif token in words.other_words:
            print "other words " + token
            outfile.write("call "+token+ "\n")
            words.copy_word(token)
        elif token == "IF":
            print token
            outfile.write("cjump then"+str(ifthen_count)+"\n")
        elif token == "THEN":
            outfile.write("then"+str(ifthen_count) + ":\n")
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
        
outfile.write("jump end\n")
outfile.write(words.wordlines)
outfile.write("end: nop\n")
