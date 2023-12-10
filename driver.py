import sys
from antlr4 import *
from P1Lexer import P1Lexer
from P1Parser import P1Parser


def main(argv):
    if len(sys.argv) > 1:
        ins = FileStream(sys.argv[1])
    else:
        ins = InputStream(sys.stdin.readline())

    lexer = P1Lexer(ins)
    tokens = CommonTokenStream(lexer)
    parser = P1Parser(tokens)
    tree = parser.start()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)