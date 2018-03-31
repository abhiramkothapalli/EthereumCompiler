//Copyright 2017 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.

/**
   
   Solidify.cpp
   Purpose: Compiles LLVM IR to Solidity. Uses class Module Pass to
   start execution flow. Uses InstVisitor to handle visiting individual
   instructions.

   @author: Abhiram Kothapalli
   @version: 1.0 June 21, 2017   

   TODO

   -Find better way to define Code, this gives errors with outs()
   -Indenting
   -Nested branching

*/


#include <iostream>
#include <unordered_set>
#include <sstream>
#include <string>
#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/InstVisitor.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
using namespace llvm;

#define Code errs()

namespace {
  class SolWriter : public ModulePass, public InstVisitor<SolWriter, void> {

  public:
    
    static char ID;

    SolWriter() : ModulePass(ID) {}

    //Pointer naming information
    std::map <Value *, int> pointerName;
    int pointerCounter = 0;

    //indent information
    int indent = 0;

    //Block visited information
    std::map <BasicBlock *, int> visitedBlocks; 

    virtual llvm::StringRef getPassName() const { return "Solidity pass"; }

    virtual bool runOnModule(Module &M){
      visit(M);
      return false;
    }

    //Block Visitors
    void visit(Module &M);
    void visit(Function &F);
    void visit(BasicBlock &B);

    //Instruction Visitors
    void visit(Instruction &I);
    void visitAllocaInst(AllocaInst  &I);
    void visitReturnInst(ReturnInst &I);
    void visitBinaryOperator(Instruction &I);
    void visitBranchInst(BranchInst &I);
    void visitCallInst(CallInst &I);
    void visitICmpInst(ICmpInst & I);
    void visitLoadInst(LoadInst & I);
    void visitStoreInst(StoreInst &I);
    void visitTruncInst(TruncInst &I);
    void visitUnreachableInst(UnreachableInst &I);
    void visitZExtInst(ZExtInst &I);
    void visitInstruction(Instruction &I);

    //Writer Methods
    void writeConstant(Value & Operand);
    void writeContractName(Module &M);
    void writeIndent(int indent);
    void writeOperand(Value & Operand);
    void writeType(Type *Ty);

    //Helper Methods
    int getAvailableInt();
    std::string getValueName(Value & value);
    
  };
}

/* WRITER METHODS */

void SolWriter::writeConstant(Value & Operand){
  
  if(Function * F = dyn_cast<Function>(&Operand)){
    Code << F->getName();
    return;
  }
  
  if(ConstantExpr *CE = dyn_cast<ConstantExpr>(&Operand)){

    Code << "Unhandled ConstExpr";
    return;
  }

  if(ConstantInt *CI = dyn_cast<ConstantInt>(&Operand)){
    /* TODO this will probably break */
    Code << CI->getSExtValue();
    return;
  }

  switch(Operand.getType()->getTypeID()){
  case Type::PointerTyID:
    if(GlobalValue *GV = dyn_cast<GlobalValue>(&Operand)){
      Code << getValueName(*GV);
    }
  }
  
  //Code << "UNHANDLED_CONST";

}

void SolWriter::writeContractName(Module &M){
  /* TODO - Contract Name */
  Code << "CONTRACT";
}

void SolWriter::writeIndent(int indent){
  int i = indent;
  while(i){
    Code << "    ";
    i--;
  }
}

void SolWriter::writeOperand(Value & Operand){


  Constant * CV = dyn_cast<Constant>(&Operand);
  if(CV){
    writeConstant(*CV);
  }
  else{
    Code << getValueName(Operand);
  }
}

void SolWriter::writeType(Type *Ty){

  switch(Ty->getTypeID()){
  case Type::VoidTyID:
    Code << "Unhandled Type: Void";
    break;
  case Type::IntegerTyID: {
    //TODO - handle signed/unsigned
    unsigned numbits = cast<IntegerType>(Ty)->getBitWidth();
    if(numbits == 1)
      Code << "bool"; 
    else if (numbits % 8 == 0 && numbits <= 256)
      Code << "int" << std::to_string(numbits);
    else
      Code << "Unhandled Error creating integer";
    break;
  }
  case Type::FloatTyID:
    //No floats in solidity
    Code << "Unhandled Error creating float";
    break;
  case Type::DoubleTyID:
    //No doubles in solidity
    Code << "Unhandled Error creating double";
    break;
  case Type::VectorTyID:
    Code << "Unhandled Type: Vector";
    break;
  case Type::FunctionTyID:
    Code << "Unhandled Type: Function";
    break;
  case Type::StructTyID:
    Code << "Unhandled Type: Struct";
    break;
  case Type::PointerTyID:
    Code << "Unhandled Type: Pointer";
    break;
  case Type::ArrayTyID: {
    ArrayType *ATy = cast<ArrayType>(Ty);
    unsigned NumElements = ATy->getNumElements();
    if(NumElements == 0) NumElements = 1; 
    writeType(ATy->getElementType());
    Code << "[" << std::to_string(NumElements) << "]";
    break;
  }
  default:
    Code << "Unhandled Type Unhandled";
    break;
  } 
}

/* HELPER METHODS */

std::string SolWriter::getValueName(Value & value){

  std::string name = value.getName();

  if(name.empty()){
    std::stringstream ss;
    if(pointerName.find(&value) == pointerName.end()){
      pointerName[&value] = pointerCounter;
      pointerCounter++;
    } 
    ss << "tmp";
    ss << pointerName[&value];
    name = ss.str();
  }
  
  return name;
}


/* BLOCK VISITORS */

void SolWriter::visit(Module &M){

  //print header
  Code <<  "/*";
  Code << "Compiled by LLVM pass Solidify";
  Code <<  "*/\n\n";
  Code <<  "pragma solidity 0.0.0; //TODO fix this pragma\n";
  Code << "\n";

  Code << "contract ";
  writeContractName(M);
  Code << " {\n\n";


  //print out globals
  for(Module::global_iterator G = M.global_begin(), E = M.global_end(); G != E; ++G){

    writeType((*G).getType()->getElementType());
    Code << " ";
    Code << getValueName(*G);
    Code << " = ";
    writeOperand(*G->getInitializer());
    Code << ";\n";

  }
  
  InstVisitor::visit(M);


  Code << "}\n";
    
}

void SolWriter::visit(Function &F){

  //Reset naming variables
  pointerName = {};
  pointerCounter = 0;

  Code << "\n";
  Code << "function " << F.getName();
  Code << "(";

  //print args
  int numparams = F.getFunctionType()->getNumParams();
  int counter = 0;
  for(Function::arg_iterator A = F.arg_begin(), E = F.arg_end(); A != E; ++A){
    writeType((*A).getType());
    Code << " ";
    Code << getValueName(*A);

    counter++;
    if(counter != numparams){
      Code << ", ";
    }
  }

  Code << ")";
  Code << " returns (";
  writeType(F.getReturnType());
  Code << ")";

  Code << " {\n\n";

  InstVisitor::visit(F);
  
  Code << "\n}\n";
  Code << "\n"; 
    
}

void SolWriter::visit(BasicBlock &BB){

  //visit block only if it is not marked as visited
  if(visitedBlocks.find(&BB) == visitedBlocks.end()){
    visitedBlocks[&BB] = 1;
    InstVisitor::visit(BB);
  }
  
}


/* INSTRUCTION VISITORS */

void SolWriter::visit(Instruction &I){
  //Code << I << ": ";
  InstVisitor::visit(I);

}


void SolWriter::visitAllocaInst(AllocaInst &I){
  writeType(I.getType()->getElementType());
  Code << " ";
  Code << getValueName(I);
  Code << ";\n";
    
}

void SolWriter::visitReturnInst(ReturnInst &I){

  bool isStructReturn = I.getParent()->getParent()->hasStructRetAttr();
  if (isStructReturn){
    Code << "Unhandled struct return " << I << "\n";
  }


  if(I.getNumOperands()){

    Code << "return ";
    writeOperand(*(I.getOperand(0)));
    Code << ";\n";
  }
  else {
    Code << "Unhandled return void " << I << "\n";
  }

}


void SolWriter::visitBinaryOperator(Instruction &I){

  if(I.getType()->isPointerTy()){
    Code << "Unhandled pointer type in binary operator";
  }

  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";

  //print first operand
  writeOperand(*(I.getOperand(0)));

  //print operator
  switch (I.getOpcode()) {
  case Instruction::Add:
  case Instruction::FAdd: Code << " + "; break;
  case Instruction::Sub:
  case Instruction::FSub: Code << " - "; break;
  case Instruction::Mul:
  case Instruction::FMul: Code << " * "; break;
  case Instruction::URem:
  case Instruction::SRem:
  case Instruction::FRem: Code << " % "; break;
  case Instruction::UDiv:
  case Instruction::SDiv:
  case Instruction::FDiv: Code << " / "; break;
  case Instruction::And:  Code << " & "; break;
  case Instruction::Or:   Code << " | "; break;
  case Instruction::Xor:  Code << " ^ "; break;
  case Instruction::Shl : Code << " << "; break;
  case Instruction::LShr:
  case Instruction::AShr: Code << " >> "; break;
  default: Code << "Unhandled bad binary instruction\n"; 
  }

  //print second operand
  writeOperand(*(I.getOperand(1)));

  Code << ";\n";

}


void SolWriter::visitBranchInst(BranchInst &I){

  /* TODO this implementation is broken */
  /* TODO this implementation cannot handle for loops */
  /* TODO this implementation can only handle single layer nesting */


  if(I.isConditional()){

    BasicBlock * successor_1 = I.getSuccessor(0); 
    BasicBlock * successor_2 = I.getSuccessor(1);

    Value * successor_1_end = (*(--successor_1->end())).getOperand(0);
    Value * successor_2_end = (*(--successor_2->end())).getOperand(0);
    
    if(successor_1_end == successor_2_end){

      //We are in an if/else clause

      Code << "\n";
      writeIndent(indent);
      Code << "if (";
      writeOperand(*(I.getCondition()));
      Code << ") {\n"; 
      visit(*successor_1);    
      Code << "} else {\n"; 
      visit(*successor_2); 
      Code << "}\n\n";


    } else {
      //we are not in if else clause
      Code << "\n";
      writeIndent(indent);

      if(successor_1_end == I.getParent()){
	//we are in while loop
	Code << "while";
      } else {
	//we are in if loop
	Code << "if";
      }	

      Code << " (";
      writeOperand(*(I.getCondition()));
      Code << ") {\n";
      visit(*successor_1);
      writeIndent(indent);
      Code << "}\n\n"; 
      
    }

	
    
  } else {

    /*TODO strong assumption that doing nothing works */
    //Code << "//Unhandled non-conditional branches: " << I << "\n";
    
  }
  
}

void SolWriter::visitCallInst(CallInst &I){

  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";
  Code << I.getCalledFunction()->getName().str();

  Code << "(";

  int numargs = I.getNumArgOperands();
  for(int i = 0; i < numargs; ++i){
    writeOperand(*I.getArgOperand(i));
    if(i != numargs - 1){
      Code << ", ";
    }
  }

  
  Code << ");\n";
  

}

void SolWriter::visitICmpInst(ICmpInst &I){

  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";

  //print first operand
  writeOperand(*I.getOperand(0));

  //print operator
  switch(I.getPredicate()){
  case ICmpInst::ICMP_EQ:  Code << " == "; break;
  case ICmpInst::ICMP_NE:  Code << " != "; break;
  case ICmpInst::ICMP_ULE:
  case ICmpInst::ICMP_SLE: Code << " <= "; break;
  case ICmpInst::ICMP_UGE:
  case ICmpInst::ICMP_SGE: Code << " >= "; break;
  case ICmpInst::ICMP_ULT:
  case ICmpInst::ICMP_SLT: Code << " < "; break;
  case ICmpInst::ICMP_UGT:
  case ICmpInst::ICMP_SGT: Code << " > "; break;
  default: Code << "Unhandled invalid icmp predicate " << I;
  }

  //print second operator
  writeOperand(*I.getOperand(1));

  Code << ";\n";
  
}

void SolWriter::visitLoadInst(LoadInst &I){

  /* TODO this will probably break */
  
  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";
  writeOperand(*I.getOperand(0));
  Code << ";\n";
  
}

void SolWriter::visitStoreInst(StoreInst & I){

  /* TODO this will probably break */

  //type is done here and allocate is removed
  //slight optimization, might have return alloca later
  //especially if we are using arrays
  //comment out alloca if this needs to be used
  //PointerType * ptr = dyn_cast<PointerType>((*I.getOperand(1)).getType());
  //writeType(ptr->getElementType());
  //Code << " ";

  
  writeOperand(*I.getOperand(1));
  Code << " = ";
  writeOperand(*I.getOperand(0));
  Code << ";\n";
}

void SolWriter::visitTruncInst(TruncInst & I){
  /* TODO truncation might be unexpected in Solidity */

  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";
  Code << getValueName(*I.getOperand(0));
  Code << " //truncation\n";
   
}

void SolWriter::visitUnreachableInst(UnreachableInst &I){
  Code << "/* Unhandled Instruction (Unreachable): " << I;
}

void SolWriter::visitZExtInst(ZExtInst &I){
  writeType(I.getType());
  Code << " ";
  Code << getValueName(I);
  Code << " = ";
  Code << getValueName(*I.getOperand(0));
  Code << " //zero extend\n";
}

void SolWriter::visitInstruction(Instruction &I){
  //default behavior
  Code << "/*UNHANDLED INSTRUCTION: " << I << "*/\n";
}


/* REGISTER THE PASS */

char SolWriter::ID = 0;
static RegisterPass<SolWriter> X("solidify", "Solidify Pass",
				 false /* Only looks at CFG */,
				 false /* Analysis Pass */);
