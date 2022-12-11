# Coding Kata Runbook

Everyone develops their own style for solving these.  I suggest using IntelliJ to
get practice with testing, debugging, intellisense, navigating the tool and setting up basic structural code.

## Setup the project
These steps will be the same for every kata.

- Launch IntelliJ
- Select File -> New -> Project
    - Name it ProjectEuler.{number}.{title}   eg ProjectEuler.001.MultiplesOf3or5
    - Check "Add Sample Code"
    - Set language to Java
    - Click the Create Button
    - Click the Run Button and confirm the Console Output says "hello world"

## Setup the kata scaffolding
These steps will be similar for every kata.

- Create a calculate method stub. Eventually this is where you'll put your logic.

```Java
public static int calculate(int target) {
    return 0; 
}
```

- Create Test Runner & helper functions

```Java
//Call calculate, comparing the result with the expected result.. printing PASS or FAIL accordingly
public static void testCalculate(int target, int expected) {...}
```

- Create Tests (start with the one ProjectEuler gives you, along with a few that are close that you can calculate by hand)
```Java
testCalculate(10, 23);
testCalculate(11, 23+10);
testCalculate(12, 23+10);
testCalculate(13, 23+10+12);
testCalculate(15, 23+10+12);
testCalculate(16, 23+10+12+15);
```

## Finally.. Try to solve the problem

- Try to implement calculate using whatever methodology you are comfortable with
  -- Just wing it (many people just do this)
  -- Test Driven Development (interviewers love this approach)
  -- Think about how you solve it as a human, and try to reproduce that in code
- Once your tests are passing, add one more test:
```JS
testCalculate(1000, -1)
```
- Run that test to get your answer!
>> FAIL: expected -1 got 233168
- Check your answer in ProjecEuler
  -- Go here: https://projecteuler.net/archives
  -- Click your problem
  -- Enter your answer in the answer box
  -- Celebrate if you got it right.. debug if not!

## Extra Credit
- Think about alternate approaches.. try at least one (but don't delete your solution.. create a second method)
- Google to look for other solutions and try out any that seem interesting

