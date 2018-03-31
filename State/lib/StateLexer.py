# Generated from grammars/State.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\6\5")
        buf.write("\66\n\5\r\5\16\5\67\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\6\16d\n\16\r\16")
        buf.write("\16\16e\3\17\6\17i\n\17\r\17\16\17j\3\17\3\17\2\2\20\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\3\2\5\5\2\62;CHch\5\2C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\2p\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5\'\3\2\2\2\7")
        buf.write("/\3\2\2\2\t\61\3\2\2\2\139\3\2\2\2\r?\3\2\2\2\17A\3\2")
        buf.write("\2\2\21C\3\2\2\2\23E\3\2\2\2\25H\3\2\2\2\27S\3\2\2\2\31")
        buf.write("\\\3\2\2\2\33c\3\2\2\2\35h\3\2\2\2\37 \7O\2\2 !\7c\2\2")
        buf.write("!\"\7e\2\2\"#\7j\2\2#$\7k\2\2$%\7p\2\2%&\7g\2\2&\4\3\2")
        buf.write("\2\2\'(\7c\2\2()\7f\2\2)*\7f\2\2*+\7t\2\2+,\7g\2\2,-\7")
        buf.write("u\2\2-.\7u\2\2.\6\3\2\2\2/\60\7?\2\2\60\b\3\2\2\2\61\62")
        buf.write("\7\62\2\2\62\63\7z\2\2\63\65\3\2\2\2\64\66\t\2\2\2\65")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\n")
        buf.write("\3\2\2\29:\7u\2\2:;\7v\2\2;<\7c\2\2<=\7v\2\2=>\7g\2\2")
        buf.write(">\f\3\2\2\2?@\7}\2\2@\16\3\2\2\2AB\7\177\2\2B\20\3\2\2")
        buf.write("\2CD\7.\2\2D\22\3\2\2\2EF\7q\2\2FG\7t\2\2G\24\3\2\2\2")
        buf.write("HI\7v\2\2IJ\7t\2\2JK\7c\2\2KL\7p\2\2LM\7u\2\2MN\7k\2\2")
        buf.write("NO\7v\2\2OP\7k\2\2PQ\7q\2\2QR\7p\2\2R\26\3\2\2\2ST\7t")
        buf.write("\2\2TU\7g\2\2UV\7s\2\2VW\7w\2\2WX\7k\2\2XY\7t\2\2YZ\7")
        buf.write("g\2\2Z[\7u\2\2[\30\3\2\2\2\\]\7u\2\2]^\7v\2\2^_\7c\2\2")
        buf.write("_`\7t\2\2`a\7v\2\2a\32\3\2\2\2bd\t\3\2\2cb\3\2\2\2de\3")
        buf.write("\2\2\2ec\3\2\2\2ef\3\2\2\2f\34\3\2\2\2gi\t\4\2\2hg\3\2")
        buf.write("\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b\17\2")
        buf.write("\2m\36\3\2\2\2\6\2\67ej\3\b\2\2")
        return buf.getvalue()


class StateLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MACHINE = 1
    ADDRESS = 2
    ASSIGN = 3
    HEXADDR = 4
    ST = 5
    OPENBRACE = 6
    CLOSEBRACE = 7
    COMMA = 8
    OR = 9
    TRANSITION = 10
    REQUIRES = 11
    START = 12
    ID = 13
    WHITESPACE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Machine'", "'address'", "'='", "'state'", "'{'", "'}'", "','", 
            "'or'", "'transition'", "'requires'", "'start'" ]

    symbolicNames = [ "<INVALID>",
            "MACHINE", "ADDRESS", "ASSIGN", "HEXADDR", "ST", "OPENBRACE", 
            "CLOSEBRACE", "COMMA", "OR", "TRANSITION", "REQUIRES", "START", 
            "ID", "WHITESPACE" ]

    ruleNames = [ "MACHINE", "ADDRESS", "ASSIGN", "HEXADDR", "ST", "OPENBRACE", 
                  "CLOSEBRACE", "COMMA", "OR", "TRANSITION", "REQUIRES", 
                  "START", "ID", "WHITESPACE" ]

    grammarFileName = "State.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


