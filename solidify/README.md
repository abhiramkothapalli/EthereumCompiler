Copyright 2017 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.

Solidify, An LLVM pass to convert LLVM IR into solidity

Dependencies:

    $ LLVM
    $ cmake

Installing LLVM from source:

    $ mkdir mybuilddir
    $ cd mybuilddir
    $ cmake path/to/llvm/source/root
    $ cmake --build .
    $ cmake --build . --target install

Build Passes:

    $ ./build/buildscript

Run Tests:

    $ ./tests/runtests
