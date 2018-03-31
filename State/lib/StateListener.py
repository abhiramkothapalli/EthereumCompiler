# Generated from grammars/State.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StateParser import StateParser
else:
    from StateParser import StateParser

# This class defines a complete listener for a parse tree produced by StateParser.
class StateListener(ParseTreeListener):

    # Enter a parse tree produced by StateParser#contract.
    def enterContract(self, ctx:StateParser.ContractContext):
        pass

    # Exit a parse tree produced by StateParser#contract.
    def exitContract(self, ctx:StateParser.ContractContext):
        pass


    # Enter a parse tree produced by StateParser#machine.
    def enterMachine(self, ctx:StateParser.MachineContext):
        pass

    # Exit a parse tree produced by StateParser#machine.
    def exitMachine(self, ctx:StateParser.MachineContext):
        pass


    # Enter a parse tree produced by StateParser#address.
    def enterAddress(self, ctx:StateParser.AddressContext):
        pass

    # Exit a parse tree produced by StateParser#address.
    def exitAddress(self, ctx:StateParser.AddressContext):
        pass


    # Enter a parse tree produced by StateParser#st.
    def enterSt(self, ctx:StateParser.StContext):
        pass

    # Exit a parse tree produced by StateParser#st.
    def exitSt(self, ctx:StateParser.StContext):
        pass


    # Enter a parse tree produced by StateParser#transition.
    def enterTransition(self, ctx:StateParser.TransitionContext):
        pass

    # Exit a parse tree produced by StateParser#transition.
    def exitTransition(self, ctx:StateParser.TransitionContext):
        pass


    # Enter a parse tree produced by StateParser#disjunction.
    def enterDisjunction(self, ctx:StateParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by StateParser#disjunction.
    def exitDisjunction(self, ctx:StateParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by StateParser#conjunction.
    def enterConjunction(self, ctx:StateParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by StateParser#conjunction.
    def exitConjunction(self, ctx:StateParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by StateParser#start.
    def enterStart(self, ctx:StateParser.StartContext):
        pass

    # Exit a parse tree produced by StateParser#start.
    def exitStart(self, ctx:StateParser.StartContext):
        pass


