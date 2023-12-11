# Generated from P1.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,0,1,0,1,1,1,1,4,1,60,8,1,11,1,12,1,61,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,74,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,84,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,95,8,4,10,4,
        12,4,98,9,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,114,8,5,1,5,1,5,1,5,1,5,4,5,120,8,5,11,5,12,5,121,5,
        5,124,8,5,10,5,12,5,127,9,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,135,8,7,
        1,7,1,7,1,8,1,8,3,8,141,8,8,1,9,1,9,5,9,145,8,9,10,9,12,9,148,9,
        9,1,10,1,10,5,10,152,8,10,10,10,12,10,155,9,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,167,8,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,3,12,178,8,12,1,12,1,12,3,12,182,8,12,
        1,12,1,12,3,12,186,8,12,1,13,3,13,189,8,13,1,13,4,13,192,8,13,11,
        13,12,13,193,1,14,1,14,1,15,3,15,199,8,15,1,15,4,15,202,8,15,11,
        15,12,15,203,1,15,1,15,5,15,208,8,15,10,15,12,15,211,9,15,1,15,1,
        15,4,15,215,8,15,11,15,12,15,216,3,15,219,8,15,1,16,1,16,1,16,5,
        16,224,8,16,10,16,12,16,227,9,16,1,16,1,16,1,16,1,16,5,16,233,8,
        16,10,16,12,16,236,9,16,1,16,3,16,239,8,16,1,17,1,17,1,17,1,17,3,
        17,245,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,254,8,18,1,19,
        1,19,1,19,1,19,5,19,260,8,19,10,19,12,19,263,9,19,3,19,265,8,19,
        1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,
        1,24,4,24,281,8,24,11,24,12,24,282,1,24,0,1,10,25,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,9,1,0,43,
        43,1,1,47,47,1,0,17,18,2,0,20,20,43,43,2,0,22,22,43,43,2,0,16,16,
        26,29,1,0,30,34,1,0,35,40,1,0,41,42,302,0,51,1,0,0,0,2,57,1,0,0,
        0,4,73,1,0,0,0,6,83,1,0,0,0,8,85,1,0,0,0,10,113,1,0,0,0,12,128,1,
        0,0,0,14,134,1,0,0,0,16,140,1,0,0,0,18,142,1,0,0,0,20,149,1,0,0,
        0,22,166,1,0,0,0,24,168,1,0,0,0,26,188,1,0,0,0,28,195,1,0,0,0,30,
        198,1,0,0,0,32,238,1,0,0,0,34,244,1,0,0,0,36,253,1,0,0,0,38,255,
        1,0,0,0,40,268,1,0,0,0,42,270,1,0,0,0,44,272,1,0,0,0,46,274,1,0,
        0,0,48,276,1,0,0,0,50,52,3,4,2,0,51,50,1,0,0,0,52,53,1,0,0,0,53,
        51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,56,1,1,0,0,
        0,57,59,5,48,0,0,58,60,3,4,2,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,
        1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,49,0,0,64,3,1,0,0,0,
        65,66,3,6,3,0,66,67,5,43,0,0,67,74,1,0,0,0,68,74,3,8,4,0,69,74,3,
        14,7,0,70,71,3,16,8,0,71,72,5,43,0,0,72,74,1,0,0,0,73,65,1,0,0,0,
        73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,74,5,1,0,0,0,75,76,5,45,
        0,0,76,77,3,42,21,0,77,78,3,36,18,0,78,84,1,0,0,0,79,80,5,45,0,0,
        80,81,3,42,21,0,81,82,3,48,24,0,82,84,1,0,0,0,83,75,1,0,0,0,83,79,
        1,0,0,0,84,7,1,0,0,0,85,86,5,1,0,0,86,87,3,10,5,0,87,88,5,2,0,0,
        88,96,3,2,1,0,89,90,5,3,0,0,90,91,3,10,5,0,91,92,5,2,0,0,92,93,3,
        2,1,0,93,95,1,0,0,0,94,89,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,
        97,1,0,0,0,97,101,1,0,0,0,98,96,1,0,0,0,99,100,5,4,0,0,100,102,3,
        2,1,0,101,99,1,0,0,0,101,102,1,0,0,0,102,9,1,0,0,0,103,104,6,5,-1,
        0,104,114,3,28,14,0,105,114,3,12,6,0,106,107,5,5,0,0,107,108,3,10,
        5,0,108,109,5,6,0,0,109,114,1,0,0,0,110,111,5,7,0,0,111,114,3,10,
        5,2,112,114,5,45,0,0,113,103,1,0,0,0,113,105,1,0,0,0,113,106,1,0,
        0,0,113,110,1,0,0,0,113,112,1,0,0,0,114,125,1,0,0,0,115,119,10,4,
        0,0,116,117,3,46,23,0,117,118,3,10,5,0,118,120,1,0,0,0,119,116,1,
        0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,1,
        0,0,0,123,115,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,
        0,0,0,126,11,1,0,0,0,127,125,1,0,0,0,128,129,3,36,18,0,129,130,3,
        44,22,0,130,131,3,36,18,0,131,13,1,0,0,0,132,135,3,22,11,0,133,135,
        3,24,12,0,134,132,1,0,0,0,134,133,1,0,0,0,135,136,1,0,0,0,136,137,
        3,2,1,0,137,15,1,0,0,0,138,141,3,18,9,0,139,141,3,20,10,0,140,138,
        1,0,0,0,140,139,1,0,0,0,141,17,1,0,0,0,142,146,5,8,0,0,143,145,8,
        0,0,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,
        0,0,0,147,19,1,0,0,0,148,146,1,0,0,0,149,153,5,47,0,0,150,152,8,
        1,0,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,
        0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,5,47,0,0,157,21,1,
        0,0,0,158,159,5,9,0,0,159,160,3,10,5,0,160,161,5,2,0,0,161,167,1,
        0,0,0,162,163,5,10,0,0,163,164,3,10,5,0,164,165,5,11,0,0,165,167,
        1,0,0,0,166,158,1,0,0,0,166,162,1,0,0,0,167,23,1,0,0,0,168,169,5,
        12,0,0,169,170,5,45,0,0,170,185,5,13,0,0,171,172,5,45,0,0,172,186,
        5,2,0,0,173,174,5,14,0,0,174,177,3,26,13,0,175,176,5,15,0,0,176,
        178,3,26,13,0,177,175,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,
        180,5,15,0,0,180,182,3,26,13,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
        183,1,0,0,0,183,184,5,11,0,0,184,186,1,0,0,0,185,171,1,0,0,0,185,
        173,1,0,0,0,186,25,1,0,0,0,187,189,5,16,0,0,188,187,1,0,0,0,188,
        189,1,0,0,0,189,191,1,0,0,0,190,192,5,44,0,0,191,190,1,0,0,0,192,
        193,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,27,1,0,0,0,195,196,
        7,2,0,0,196,29,1,0,0,0,197,199,5,16,0,0,198,197,1,0,0,0,198,199,
        1,0,0,0,199,218,1,0,0,0,200,202,5,44,0,0,201,200,1,0,0,0,202,203,
        1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,209,
        5,19,0,0,206,208,5,44,0,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,219,1,0,0,0,211,209,1,0,0,0,212,214,
        5,19,0,0,213,215,5,44,0,0,214,213,1,0,0,0,215,216,1,0,0,0,216,214,
        1,0,0,0,216,217,1,0,0,0,217,219,1,0,0,0,218,201,1,0,0,0,218,212,
        1,0,0,0,219,31,1,0,0,0,220,225,5,20,0,0,221,224,5,21,0,0,222,224,
        8,3,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,227,1,0,0,0,225,223,
        1,0,0,0,225,226,1,0,0,0,226,228,1,0,0,0,227,225,1,0,0,0,228,239,
        5,20,0,0,229,234,5,22,0,0,230,233,5,23,0,0,231,233,8,4,0,0,232,230,
        1,0,0,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,
        1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,239,5,22,0,0,238,220,
        1,0,0,0,238,229,1,0,0,0,239,33,1,0,0,0,240,245,3,28,14,0,241,245,
        3,26,13,0,242,245,3,30,15,0,243,245,3,32,16,0,244,240,1,0,0,0,244,
        241,1,0,0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,35,1,0,0,0,246,254,
        5,45,0,0,247,254,3,34,17,0,248,249,5,5,0,0,249,250,3,36,18,0,250,
        251,5,6,0,0,251,254,1,0,0,0,252,254,3,38,19,0,253,246,1,0,0,0,253,
        247,1,0,0,0,253,248,1,0,0,0,253,252,1,0,0,0,254,37,1,0,0,0,255,264,
        5,24,0,0,256,261,3,36,18,0,257,258,5,15,0,0,258,260,3,36,18,0,259,
        257,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,264,256,1,0,0,0,264,265,1,0,0,0,265,
        266,1,0,0,0,266,267,5,25,0,0,267,39,1,0,0,0,268,269,7,5,0,0,269,
        41,1,0,0,0,270,271,7,6,0,0,271,43,1,0,0,0,272,273,7,7,0,0,273,45,
        1,0,0,0,274,275,7,8,0,0,275,47,1,0,0,0,276,280,3,36,18,0,277,278,
        3,40,20,0,278,279,3,36,18,0,279,281,1,0,0,0,280,277,1,0,0,0,281,
        282,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,49,1,0,0,0,34,53,
        61,73,83,96,101,113,121,125,134,140,146,153,166,177,181,185,188,
        193,198,203,209,216,218,223,225,232,234,238,244,253,261,264,282
    ]

class P1Parser ( Parser ):

    grammarFileName = "P1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if '", "':'", "'elif '", "'else:'", 
                     "'('", "')'", "'not '", "'#'", "'while '", "'while('", 
                     "'):'", "'for '", "' in '", "'range('", "','", "'-'", 
                     "'True'", "'False'", "'.'", "'\"'", "'\\\"'", "'''", 
                     "'\\''", "'['", "']'", "'+'", "'*'", "'/'", "'%'", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'<'", "'>'", 
                     "'>='", "'<='", "'=='", "'!='", "'and'", "'or'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'''''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NL", "DIGIT", 
                      "VAR", "SPACE", "THREEQUOTES", "INDENT", "DEDENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_line = 2
    RULE_assign_statement = 3
    RULE_if_statement = 4
    RULE_bool_statement = 5
    RULE_comparison = 6
    RULE_loop = 7
    RULE_comment = 8
    RULE_single_line_comment = 9
    RULE_multi_line_comment = 10
    RULE_while_loop = 11
    RULE_for_loop = 12
    RULE_int = 13
    RULE_bool = 14
    RULE_float = 15
    RULE_string = 16
    RULE_literal = 17
    RULE_value = 18
    RULE_list = 19
    RULE_arith_operator = 20
    RULE_assign_operator = 21
    RULE_relat_operator = 22
    RULE_logic_operator = 23
    RULE_athm_expr = 24

    ruleNames =  [ "start", "block", "line", "assign_statement", "if_statement", 
                   "bool_statement", "comparison", "loop", "comment", "single_line_comment", 
                   "multi_line_comment", "while_loop", "for_loop", "int", 
                   "bool", "float", "string", "literal", "value", "list", 
                   "arith_operator", "assign_operator", "relat_operator", 
                   "logic_operator", "athm_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    NL=43
    DIGIT=44
    VAR=45
    SPACE=46
    THREEQUOTES=47
    INDENT=48
    DEDENT=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(P1Parser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.LineContext)
            else:
                return self.getTypedRuleContext(P1Parser.LineContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = P1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.line()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 175921860450050) != 0)):
                    break

            self.state = 55
            self.match(P1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(P1Parser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(P1Parser.DEDENT, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.LineContext)
            else:
                return self.getTypedRuleContext(P1Parser.LineContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = P1Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(P1Parser.INDENT)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.line()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 175921860450050) != 0)):
                    break

            self.state = 63
            self.match(P1Parser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(P1Parser.Assign_statementContext,0)


        def NL(self):
            return self.getToken(P1Parser.NL, 0)

        def if_statement(self):
            return self.getTypedRuleContext(P1Parser.If_statementContext,0)


        def loop(self):
            return self.getTypedRuleContext(P1Parser.LoopContext,0)


        def comment(self):
            return self.getTypedRuleContext(P1Parser.CommentContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = P1Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 65
                self.assign_statement()
                self.state = 66
                self.match(P1Parser.NL)
                pass
            elif token in [1]:
                self.state = 68
                self.if_statement()
                pass
            elif token in [9, 10, 12]:
                self.state = 69
                self.loop()
                pass
            elif token in [8, 47]:
                self.state = 70
                self.comment()
                self.state = 71
                self.match(P1Parser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(P1Parser.VAR, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(P1Parser.Assign_operatorContext,0)


        def value(self):
            return self.getTypedRuleContext(P1Parser.ValueContext,0)


        def athm_expr(self):
            return self.getTypedRuleContext(P1Parser.Athm_exprContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_assign_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_statement" ):
                listener.enterAssign_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_statement" ):
                listener.exitAssign_statement(self)




    def assign_statement(self):

        localctx = P1Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign_statement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(P1Parser.VAR)
                self.state = 76
                self.assign_operator()
                self.state = 77
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(P1Parser.VAR)
                self.state = 80
                self.assign_operator()
                self.state = 81
                self.athm_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.Bool_statementContext)
            else:
                return self.getTypedRuleContext(P1Parser.Bool_statementContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.BlockContext)
            else:
                return self.getTypedRuleContext(P1Parser.BlockContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = P1Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(P1Parser.T__0)
            self.state = 86
            self.bool_statement(0)
            self.state = 87
            self.match(P1Parser.T__1)
            self.state = 88
            self.block()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 89
                self.match(P1Parser.T__2)
                self.state = 90
                self.bool_statement(0)
                self.state = 91
                self.match(P1Parser.T__1)
                self.state = 92
                self.block()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 99
                self.match(P1Parser.T__3)
                self.state = 100
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_(self):
            return self.getTypedRuleContext(P1Parser.BoolContext,0)


        def comparison(self):
            return self.getTypedRuleContext(P1Parser.ComparisonContext,0)


        def bool_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.Bool_statementContext)
            else:
                return self.getTypedRuleContext(P1Parser.Bool_statementContext,i)


        def VAR(self):
            return self.getToken(P1Parser.VAR, 0)

        def logic_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.Logic_operatorContext)
            else:
                return self.getTypedRuleContext(P1Parser.Logic_operatorContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_bool_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_statement" ):
                listener.enterBool_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_statement" ):
                listener.exitBool_statement(self)



    def bool_statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = P1Parser.Bool_statementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_bool_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 104
                self.bool_()
                pass

            elif la_ == 2:
                self.state = 105
                self.comparison()
                pass

            elif la_ == 3:
                self.state = 106
                self.match(P1Parser.T__4)
                self.state = 107
                self.bool_statement(0)
                self.state = 108
                self.match(P1Parser.T__5)
                pass

            elif la_ == 4:
                self.state = 110
                self.match(P1Parser.T__6)
                self.state = 111
                self.bool_statement(2)
                pass

            elif la_ == 5:
                self.state = 112
                self.match(P1Parser.VAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = P1Parser.Bool_statementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_statement)
                    self.state = 115
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 119 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 116
                            self.logic_operator()
                            self.state = 117
                            self.bool_statement(0)

                        else:
                            raise NoViableAltException(self)
                        self.state = 121 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
             
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(P1Parser.ValueContext,i)


        def relat_operator(self):
            return self.getTypedRuleContext(P1Parser.Relat_operatorContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = P1Parser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.value()
            self.state = 129
            self.relat_operator()
            self.state = 130
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(P1Parser.BlockContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(P1Parser.While_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(P1Parser.For_loopContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)




    def loop(self):

        localctx = P1Parser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.state = 132
                self.while_loop()
                pass
            elif token in [12]:
                self.state = 133
                self.for_loop()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_line_comment(self):
            return self.getTypedRuleContext(P1Parser.Single_line_commentContext,0)


        def multi_line_comment(self):
            return self.getTypedRuleContext(P1Parser.Multi_line_commentContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = P1Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comment)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.single_line_comment()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.multi_line_comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_line_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.NL)
            else:
                return self.getToken(P1Parser.NL, i)

        def getRuleIndex(self):
            return P1Parser.RULE_single_line_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_line_comment" ):
                listener.enterSingle_line_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_line_comment" ):
                listener.exitSingle_line_comment(self)




    def single_line_comment(self):

        localctx = P1Parser.Single_line_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_single_line_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(P1Parser.T__7)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1117103813820414) != 0):
                self.state = 143
                _la = self._input.LA(1)
                if _la <= 0 or _la==43:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_line_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THREEQUOTES(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.THREEQUOTES)
            else:
                return self.getToken(P1Parser.THREEQUOTES, i)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.EOF)
            else:
                return self.getToken(P1Parser.EOF, i)

        def getRuleIndex(self):
            return P1Parser.RULE_multi_line_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_line_comment" ):
                listener.enterMulti_line_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_line_comment" ):
                listener.exitMulti_line_comment(self)




    def multi_line_comment(self):

        localctx = P1Parser.Multi_line_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multi_line_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(P1Parser.THREEQUOTES)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487294) != 0):
                self.state = 150
                _la = self._input.LA(1)
                if _la <= 0 or _la==-1 or _la==47:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(P1Parser.THREEQUOTES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_statement(self):
            return self.getTypedRuleContext(P1Parser.Bool_statementContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = P1Parser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_loop)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(P1Parser.T__8)
                self.state = 159
                self.bool_statement(0)
                self.state = 160
                self.match(P1Parser.T__1)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(P1Parser.T__9)
                self.state = 163
                self.bool_statement(0)
                self.state = 164
                self.match(P1Parser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.VAR)
            else:
                return self.getToken(P1Parser.VAR, i)

        def int_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.IntContext)
            else:
                return self.getTypedRuleContext(P1Parser.IntContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = P1Parser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(P1Parser.T__11)
            self.state = 169
            self.match(P1Parser.VAR)
            self.state = 170
            self.match(P1Parser.T__12)
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 171
                self.match(P1Parser.VAR)
                self.state = 172
                self.match(P1Parser.T__1)
                pass
            elif token in [14]:
                self.state = 173
                self.match(P1Parser.T__13)
                self.state = 174
                self.int_()
                self.state = 177
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 175
                    self.match(P1Parser.T__14)
                    self.state = 176
                    self.int_()


                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 179
                    self.match(P1Parser.T__14)
                    self.state = 180
                    self.int_()


                self.state = 183
                self.match(P1Parser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.DIGIT)
            else:
                return self.getToken(P1Parser.DIGIT, i)

        def getRuleIndex(self):
            return P1Parser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = P1Parser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 187
                self.match(P1Parser.T__15)


            self.state = 191 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 190
                    self.match(P1Parser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 193 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return P1Parser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)




    def bool_(self):

        localctx = P1Parser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.DIGIT)
            else:
                return self.getToken(P1Parser.DIGIT, i)

        def getRuleIndex(self):
            return P1Parser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = P1Parser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 197
                self.match(P1Parser.T__15)


            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 200
                    self.match(P1Parser.DIGIT)
                    self.state = 203 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==44):
                        break

                self.state = 205
                self.match(P1Parser.T__18)
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 206
                        self.match(P1Parser.DIGIT) 
                    self.state = 211
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass
            elif token in [19]:
                self.state = 212
                self.match(P1Parser.T__18)
                self.state = 214 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 213
                        self.match(P1Parser.DIGIT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 216 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(P1Parser.NL)
            else:
                return self.getToken(P1Parser.NL, i)

        def getRuleIndex(self):
            return P1Parser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = P1Parser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(P1Parser.T__19)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1117103812771838) != 0):
                    self.state = 223
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 221
                        self.match(P1Parser.T__20)
                        pass

                    elif la_ == 2:
                        self.state = 222
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==20 or _la==43:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass


                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 228
                self.match(P1Parser.T__19)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(P1Parser.T__21)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1117103809626110) != 0):
                    self.state = 232
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 230
                        self.match(P1Parser.T__22)
                        pass

                    elif la_ == 2:
                        self.state = 231
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==22 or _la==43:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass


                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 237
                self.match(P1Parser.T__21)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_(self):
            return self.getTypedRuleContext(P1Parser.BoolContext,0)


        def int_(self):
            return self.getTypedRuleContext(P1Parser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(P1Parser.FloatContext,0)


        def string(self):
            return self.getTypedRuleContext(P1Parser.StringContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = P1Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.bool_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.int_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.float_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(P1Parser.VAR, 0)

        def literal(self):
            return self.getTypedRuleContext(P1Parser.LiteralContext,0)


        def value(self):
            return self.getTypedRuleContext(P1Parser.ValueContext,0)


        def list_(self):
            return self.getTypedRuleContext(P1Parser.ListContext,0)


        def getRuleIndex(self):
            return P1Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = P1Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(P1Parser.VAR)
                pass
            elif token in [16, 17, 18, 19, 20, 22, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.literal()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(P1Parser.T__4)
                self.state = 249
                self.value()
                self.state = 250
                self.match(P1Parser.T__5)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(P1Parser.ValueContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = P1Parser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(P1Parser.T__23)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 52776581136416) != 0):
                self.state = 256
                self.value()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 257
                    self.match(P1Parser.T__14)
                    self.state = 258
                    self.value()
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 266
            self.match(P1Parser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return P1Parser.RULE_arith_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_operator" ):
                listener.enterArith_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_operator" ):
                listener.exitArith_operator(self)




    def arith_operator(self):

        localctx = P1Parser.Arith_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arith_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006698496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return P1Parser.RULE_assign_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_operator" ):
                listener.enterAssign_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_operator" ):
                listener.exitAssign_operator(self)




    def assign_operator(self):

        localctx = P1Parser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33285996544) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return P1Parser.RULE_relat_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelat_operator" ):
                listener.enterRelat_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelat_operator" ):
                listener.exitRelat_operator(self)




    def relat_operator(self):

        localctx = P1Parser.Relat_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_relat_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return P1Parser.RULE_logic_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_operator" ):
                listener.enterLogic_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_operator" ):
                listener.exitLogic_operator(self)




    def logic_operator(self):

        localctx = P1Parser.Logic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Athm_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(P1Parser.ValueContext,i)


        def arith_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(P1Parser.Arith_operatorContext)
            else:
                return self.getTypedRuleContext(P1Parser.Arith_operatorContext,i)


        def getRuleIndex(self):
            return P1Parser.RULE_athm_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAthm_expr" ):
                listener.enterAthm_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAthm_expr" ):
                listener.exitAthm_expr(self)




    def athm_expr(self):

        localctx = P1Parser.Athm_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_athm_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.value()
            self.state = 280 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 277
                self.arith_operator()
                self.state = 278
                self.value()
                self.state = 282 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006698496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.bool_statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bool_statement_sempred(self, localctx:Bool_statementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




