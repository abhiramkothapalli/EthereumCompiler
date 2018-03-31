//Copyright 2017 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.

#include <stdio.h>
#include <string.h>

int candidate_a = 0;
int candidate_b = 0;
int winner = -1;
int threshold = 10;

int vote(int choice){

  if(choice){
    candidate_b += 1;
  } else {
    candidate_a += 1;
  }

  return 0;

}


//returns -1 if winner is not set
int get_winner(){

  if(winner == -1 && candidate_a >= threshold){
    winner = 0;
  }

  if(winner == -1 && candidate_b >= threshold){

    winner = 1;
  }

  return winner;

}


  


