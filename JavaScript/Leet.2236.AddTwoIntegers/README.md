# Coding Kata Runbook

Everyone develops their own style for solving these.  Most people solve within Leet Code.. I suggest using IntelliJ to
get practice with testing, debugging, intellisense, navigating the tool and setting up basic structural code.

## Setup the project
These steps will be the same for every kata.

- Launch IntelliJ
- Select File -> New -> Project
    - Name it Leet.{number}.{title}   eg Leet.2236.AddTwoIntegers
    - Check "Add Sample Code"
    - Select Language = Javascript
    - Click the Create Button
    - Click the Run Button and confirm the Console Output says "hello world"

## Setup the kata scaffolding
These steps will be similar for every kata.

- Copy and paste function from Leet Code, returning something (in this case null). eg

```JS
var sum = function(num1, num2) {
  return 0;
};
```

- Create Test Runner & helper functions

```JS
//Call sum, comparing the result with the expected result... printing PASS or FAIL accordingly
var testSum = function(num1, num2, expected) {..}
```

- Create Tests (start with edge cases & leet code examples)
```JS
testSum(0, 0, 0);
testSum(1, 1, 2);
testSum(-1, 1, 0);
testSum(100, 100, 200);
testSum(-100, -100, -200);
```

- Run and verify FAILING output (you haven’t implemented sum yet!)


## Finally.. Try to solve the problem

- Try to implement sum using whatever methodology you are comfortable with
  -- Just wing it (many people just do this)
  -- Test Driven Development (interviewers love this approach)
  -- Think about how you solve it as a human, and try to reproduce that in code
- Once your tests are passing, Copy your sum code to Leet Code, and run their Tests
- Submit if their tests pass
- Celebrate if your solution is accepted.. debug if not!

## Extra Credit
- Think about alternate approaches.. try at least one (but don't delete your solution.. create a second method)
- Check out the official solution and/or other submitted solutions.
- Play around with any that seem interesting

