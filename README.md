# soccer-ranking-project


## The Problem

We want you to create a command-line application that will calculate the ranking table for a soccer league.

### Input/output

You can find the sample-input.txt and expected-output.txt files here.

The input and output will be text. Your solution should parse the provided sample-input.txt file via stdin (pipe or redirect) or by parsing a file passed by name on the command line. Your solution should output the correct result via stdout to the console.

The input contains results of games, one per line. See sample-input.txt for details. The output should be ordered from most to least points, following the format specified in expected-output.txt.

You can expect that the input will be well-formed. There is no need to add special handling for malformed input files.

### The rules

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points. If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data).

We expect the resulting output of the provided sample-input.txt file to exactly match the contents of expected-output.txt.
### Guidelines

This should be implemented in a language with which you are familiar. We would prefer that you use Haskell, Python, Scala, Javascript (Typescript preferred), Java, or C, if you are comfortable doing so. If none of these are comfortable, please choose a language that is both comfortable for you and suited to the task.

Your solution should be able to be run (and if applicable, built) from the command line. Please include appropriate scripts and instructions for running your application and your tests.

If you use other libraries installed by a common package manager (cabal, npm, pip, gradle), it is not necessary to commit the installed packages.

We write automated tests and we would like you to do so as well.

We appreciate well factored, object-oriented or functional designs.

Please document any steps necessary to run your solution and your tests.

We request that you spend no more than 2 hours on this portion of the interview.
### What to send back to LeapYear

Please send an email back to your point of contact at LeapYear with:

  - the code you used to calculate the rankings
  - your test suite code
  - simple instructions on how to install and use your code
  - the amount of time you spent on the project

### Platform support

This will be run in a unix-ish environment (OS X or Linux). If you choose to use a compiled language, please keep this in mind. Please use platform-agnostic constructs where possible (line-endings and file-path-separators are two problematic areas).

