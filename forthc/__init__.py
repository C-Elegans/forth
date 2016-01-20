#!/usr/bin/python
import words,stack_as
import sys, re, getopt
def main():
        
    whitespace = re.compile(r"[ \t\n]+")
    number = re.compile(r"-?[0-9]+")
    inputfile = ''
    outputfile = ''
    quiet = False
   
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hqi:o:",["ifile=","ofile=","quiet"])
       
        for opt, arg in opts:
            if opt == '-h':
                print 'Usage: compiler.py -i <inputfile> -o <outputfile>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
            elif opt in ("-q", "--quiet"):
                quiet = True
    except getopt.GetoptError:
        print 'Usage: compiler.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    
    
    
    if inputfile != '' and outputfile != '':
        lines = open(inputfile,"r").read()
        outfile = open(outputfile,"w")
    else:
        print "No input or output specified"
        sys.exit(-1)
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
                asm_text += "call "+token+ "\n"
                words.copy_word(token)
            elif token == "IF":
                asm_text += "cjump then"+str(ifthen_count)+"\n"
            elif token == "THEN":
                asm_text += "then"+str(ifthen_count) + ":\n"
                ifthen_count += 1
            elif token == ":":
                new_word = []
                for w_token in tokens_iter:
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
    if not quiet:
        print asm_text
    out_lines = asm_text.split("\n")
    arr = stack_as.main(out_lines)
    outfile.write(bytearray(arr))
if __name__ == "__main__":
    main()
