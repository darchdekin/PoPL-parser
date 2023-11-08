import sys
from io import StringIO
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

#Coded with support from provided class files from Dr. Ufukepte
#DISREGARD THIS FILE FOR NOW, it is a work in progress........

def main():  
    inputFile = open("project_deliverable_1_testcase.py", "r")
	for x in inputFile:
		s = InputStream(x)
		lexer = ExprLexer(s)
		stream = CommonTokenStream(lexer)
		parser = ExprParser(stream)
		tree = parser.prog()
		if parser.getNumberOfSyntaxErrors() > 0:
			print("failed: " + s)
		else:
			print("passed!")

main()
