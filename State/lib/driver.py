import sys
from antlr4 import *
from StateLexer import StateLexer
from StateParser import StateParser
from CodeGen import CodeGen
from StateListener import StateListener
 
def main(argv):
    input = FileStream(argv[1])
    lexer = StateLexer(input)
    stream = CommonTokenStream(lexer)
    parser = StateParser(stream)
    tree = parser.contract()
    listener = CodeGen()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
if __name__ == '__main__':
    main(sys.argv)
