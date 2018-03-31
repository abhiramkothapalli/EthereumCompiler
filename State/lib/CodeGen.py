from StateParser import StateParser
from StateListener import StateListener
from collections import namedtuple

class CodeGen(StateListener):

    name = None
    addresses = []
    states = []
    start = None

    '''
    Functions that keep track of visited objects in AST
    '''
    
    # Exit a parse tree produced by StateParser#contract.
    def exitContract(self, ctx:StateParser.ContractContext):
        #once we are done creating objects we will print them
        self.generate()

    # Enter a parse tree produced by StateParser#machine.
    def enterMachine(self, ctx:StateParser.MachineContext):
        self.name = ctx.ID().getText()
        pass

    # Enter a parse tree produced by StateParser#address.
    def enterAddress(self, ctx:StateParser.AddressContext):
        self.addresses.append(ctx)
        pass

    # Enter a parse tree produced by StateParser#state.
    def enterSt(self, ctx:StateParser.StContext):
        self.states.append(ctx)
        pass


    # Enter a parse tree produced by StateParser#start.
    def enterStart(self, ctx:StateParser.StartContext):
        self.start = ctx.ID().getText()
        pass


    '''
    Functions that define printing
    '''

    def print_pragma(self):
        print("pragma solidity ^0.4.13;")
        print()

    def print_contract_header(self):
        print("contract " + self.name + " {")

    def print_address(self,ctx):
        print("address " + ctx.ID().getText() + " = " + ctx.HEXADDR().getText() + ";")

    def print_addresses(self):
        print()
        for address in self.addresses:
            self.print_address(address)
        print()

    def print_address_array(self):
        print("address[] addresses = [", end="")
        for i in range(len(self.addresses)):
            print(self.addresses[i].ID().getText(), end="")
            if i != len(self.addresses) - 1:
                print(", ", end="")
        print("];")
        
        
    def print_start(self):
        print("State public current_state = State." + self.start + ";")

    def print_enum(self):
        print("enum State {", end="")
        for i in range(len(self.states)):
            print(self.states[i].ID().getText(), end="")
            if i != len(self.states) - 1:
                print(", ", end="")         
        print("}")

    def print_num_states(self):
        print("uint num_states = " + str(len(self.states)) + ";")

    def print_sigs(self):
        print("mapping (address => uint) public sigs;")

    def print_global_variables(self):
        self.print_addresses()
        self.print_address_array()
        self.print_enum()   
        self.print_num_states()
        self.print_start()
        self.print_sigs()

    def print_disjunction(self, disjunction):
        conjunctions = disjunction.conjunction()
        for i in range(len(conjunctions)):
            self.print_conjunction(conjunctions[i])
            if i != len(conjunctions) - 1:
                print(" || ", end="")

    def print_conjunction(self, conjunction):
        identities = conjunction.ID()
        for i in range(len(identities)):
            print("signed(s, " + identities[i].getText() + ")",end="")
            if i != len(identities) - 1:
                print(" && ", end="")
        

    def print_transition(self, transition):
        to_state = transition.ID().getText()
        print("if(s == State." + to_state + " && (", end="")
        self.print_disjunction(transition.disjunction())
        print(")){")
        print("current_state = s;")
        print("reset();")
        print("return;")
        print("}")
        
    def print_state(self, ctx):
        name = ctx.ID().getText()
        print("if (current_state == State." + name + ") {")
        for transition in ctx.transition():
            self.print_transition(transition)
        print("}")
        print()

    def print_transition_function(self):
        print()
        print("function transition (State s) {")
        print()
        print("sigs[msg.sender] = uint(s);")
        print()
        for state in self.states:
            self.print_state(state)
        print("}")
        print()

    def print_signed_function(self):
        print()
        print("function signed(State s, address a) returns (bool){")
        print("return sigs[a] == uint(s);")
        print("}")
        print()

    def print_reset_function(self):
        print()
        print("function reset() {")
        print("for(uint i = 0; i < addresses.length; i++){")
        print("delete sigs[addresses[i]];")
        print("}")
        print("}")
        print()
        
    def generate(self):
        self.print_pragma()
        self.print_contract_header()
        self.print_global_variables()
        self.print_signed_function()
        self.print_reset_function()
        self.print_transition_function()
        print("}")
    
