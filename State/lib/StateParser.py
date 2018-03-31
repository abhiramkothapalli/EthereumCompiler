# Generated from grammars/State.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3\2\7")
        buf.write("\2\33\n\2\f\2\16\2\36\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7=\n\7\f\7")
        buf.write("\16\7@\13\7\3\b\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2J\2\22\3\2")
        buf.write("\2\2\4!\3\2\2\2\6$\3\2\2\2\b)\3\2\2\2\n\64\3\2\2\2\f9")
        buf.write("\3\2\2\2\16A\3\2\2\2\20I\3\2\2\2\22\26\5\4\3\2\23\25\5")
        buf.write("\6\4\2\24\23\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\34\3\2\2\2\30\26\3\2\2\2\31\33\5\b\5\2\32")
        buf.write("\31\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\37\3\2\2\2\36\34\3\2\2\2\37 \5\20\t\2 \3\3\2\2\2!")
        buf.write("\"\7\3\2\2\"#\7\17\2\2#\5\3\2\2\2$%\7\4\2\2%&\7\17\2\2")
        buf.write("&\'\7\5\2\2\'(\7\6\2\2(\7\3\2\2\2)*\7\7\2\2*+\7\17\2\2")
        buf.write("+/\7\b\2\2,.\5\n\6\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/")
        buf.write("\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62\63\7\t\2\2\63")
        buf.write("\t\3\2\2\2\64\65\7\f\2\2\65\66\7\17\2\2\66\67\7\r\2\2")
        buf.write("\678\5\f\7\28\13\3\2\2\29>\5\16\b\2:;\7\13\2\2;=\5\16")
        buf.write("\b\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\r\3\2\2")
        buf.write("\2@>\3\2\2\2AF\7\17\2\2BC\7\n\2\2CE\7\17\2\2DB\3\2\2\2")
        buf.write("EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\17\3\2\2\2HF\3\2\2\2I")
        buf.write("J\7\16\2\2JK\7\5\2\2KL\7\17\2\2L\21\3\2\2\2\7\26\34/>")
        buf.write("F")
        return buf.getvalue()


class StateParser ( Parser ):

    grammarFileName = "State.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Machine'", "'address'", "'='", "<INVALID>", 
                     "'state'", "'{'", "'}'", "','", "'or'", "'transition'", 
                     "'requires'", "'start'" ]

    symbolicNames = [ "<INVALID>", "MACHINE", "ADDRESS", "ASSIGN", "HEXADDR", 
                      "ST", "OPENBRACE", "CLOSEBRACE", "COMMA", "OR", "TRANSITION", 
                      "REQUIRES", "START", "ID", "WHITESPACE" ]

    RULE_contract = 0
    RULE_machine = 1
    RULE_address = 2
    RULE_st = 3
    RULE_transition = 4
    RULE_disjunction = 5
    RULE_conjunction = 6
    RULE_start = 7

    ruleNames =  [ "contract", "machine", "address", "st", "transition", 
                   "disjunction", "conjunction", "start" ]

    EOF = Token.EOF
    MACHINE=1
    ADDRESS=2
    ASSIGN=3
    HEXADDR=4
    ST=5
    OPENBRACE=6
    CLOSEBRACE=7
    COMMA=8
    OR=9
    TRANSITION=10
    REQUIRES=11
    START=12
    ID=13
    WHITESPACE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ContractContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def machine(self):
            return self.getTypedRuleContext(StateParser.MachineContext,0)


        def start(self):
            return self.getTypedRuleContext(StateParser.StartContext,0)


        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateParser.AddressContext)
            else:
                return self.getTypedRuleContext(StateParser.AddressContext,i)


        def st(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateParser.StContext)
            else:
                return self.getTypedRuleContext(StateParser.StContext,i)


        def getRuleIndex(self):
            return StateParser.RULE_contract

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContract" ):
                listener.enterContract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContract" ):
                listener.exitContract(self)




    def contract(self):

        localctx = StateParser.ContractContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_contract)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.machine()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateParser.ADDRESS:
                self.state = 17
                self.address()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateParser.ST:
                self.state = 23
                self.st()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.start()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MachineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACHINE(self):
            return self.getToken(StateParser.MACHINE, 0)

        def ID(self):
            return self.getToken(StateParser.ID, 0)

        def getRuleIndex(self):
            return StateParser.RULE_machine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMachine" ):
                listener.enterMachine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMachine" ):
                listener.exitMachine(self)




    def machine(self):

        localctx = StateParser.MachineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_machine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(StateParser.MACHINE)
            self.state = 32
            self.match(StateParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDRESS(self):
            return self.getToken(StateParser.ADDRESS, 0)

        def ID(self):
            return self.getToken(StateParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(StateParser.ASSIGN, 0)

        def HEXADDR(self):
            return self.getToken(StateParser.HEXADDR, 0)

        def getRuleIndex(self):
            return StateParser.RULE_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddress" ):
                listener.enterAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddress" ):
                listener.exitAddress(self)




    def address(self):

        localctx = StateParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(StateParser.ADDRESS)
            self.state = 35
            self.match(StateParser.ID)
            self.state = 36
            self.match(StateParser.ASSIGN)
            self.state = 37
            self.match(StateParser.HEXADDR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ST(self):
            return self.getToken(StateParser.ST, 0)

        def ID(self):
            return self.getToken(StateParser.ID, 0)

        def OPENBRACE(self):
            return self.getToken(StateParser.OPENBRACE, 0)

        def CLOSEBRACE(self):
            return self.getToken(StateParser.CLOSEBRACE, 0)

        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateParser.TransitionContext)
            else:
                return self.getTypedRuleContext(StateParser.TransitionContext,i)


        def getRuleIndex(self):
            return StateParser.RULE_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSt" ):
                listener.enterSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSt" ):
                listener.exitSt(self)




    def st(self):

        localctx = StateParser.StContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(StateParser.ST)
            self.state = 40
            self.match(StateParser.ID)
            self.state = 41
            self.match(StateParser.OPENBRACE)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateParser.TRANSITION:
                self.state = 42
                self.transition()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(StateParser.CLOSEBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSITION(self):
            return self.getToken(StateParser.TRANSITION, 0)

        def ID(self):
            return self.getToken(StateParser.ID, 0)

        def REQUIRES(self):
            return self.getToken(StateParser.REQUIRES, 0)

        def disjunction(self):
            return self.getTypedRuleContext(StateParser.DisjunctionContext,0)


        def getRuleIndex(self):
            return StateParser.RULE_transition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransition" ):
                listener.enterTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransition" ):
                listener.exitTransition(self)




    def transition(self):

        localctx = StateParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_transition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(StateParser.TRANSITION)
            self.state = 51
            self.match(StateParser.ID)
            self.state = 52
            self.match(StateParser.REQUIRES)
            self.state = 53
            self.disjunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StateParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(StateParser.ConjunctionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(StateParser.OR)
            else:
                return self.getToken(StateParser.OR, i)

        def getRuleIndex(self):
            return StateParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)




    def disjunction(self):

        localctx = StateParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.conjunction()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateParser.OR:
                self.state = 56
                self.match(StateParser.OR)
                self.state = 57
                self.conjunction()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(StateParser.ID)
            else:
                return self.getToken(StateParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StateParser.COMMA)
            else:
                return self.getToken(StateParser.COMMA, i)

        def getRuleIndex(self):
            return StateParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)




    def conjunction(self):

        localctx = StateParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(StateParser.ID)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==StateParser.COMMA:
                self.state = 64
                self.match(StateParser.COMMA)
                self.state = 65
                self.match(StateParser.ID)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(StateParser.START, 0)

        def ASSIGN(self):
            return self.getToken(StateParser.ASSIGN, 0)

        def ID(self):
            return self.getToken(StateParser.ID, 0)

        def getRuleIndex(self):
            return StateParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = StateParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(StateParser.START)
            self.state = 72
            self.match(StateParser.ASSIGN)
            self.state = 73
            self.match(StateParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





