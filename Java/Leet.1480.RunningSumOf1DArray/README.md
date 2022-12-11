# Coding Kata Runbook

Everyone develops their own style for solving these.  Most people solve within Leet Code.. I suggest using IntelliJ to 
get practice with testing, debugging, intellisense, navigating the tool and setting up basic structural code.

## Setup the project
These steps will be the same for every kata.

- Launch IntelliJ
- Select File -> New -> Project
  - Name it Leet.{number}.{title}   eg Leet.1480.RunningSumOf1DArray
  - Check "Add Sample Code"
  - Click the Create Button
  - Click the Run Button and confirm the Console Output says "hello world" 

## Setup the kata scaffolding
These steps will be similar for every kata. 

- Copy and paste function from Leet Code, returning something (in this case null). eg

```Java
public int[] runningSum(int[] nums) {
    return null;
}
```

- Create Test Runner & helper functions

```Java
//Call runningSum, comparing the result with the expected result.. printing PASS or FAIL accordingly
public void testRunningSum(int[] nums, int[] expected) {..}

// Convenience method to print out an array
public void PrintArray(int[] nums) {..}
```
Note above - you could simply use jUnit for all this test & output scaffolding... but it's good practice. When you get bored of it, you can try switching to jUnit for fun.

- Create Tests (start with edge cases & leet code examples)
```Java
//testRunningSum(new int[]{}, new int[]{});
main.testRunningSum(new int[]{1}, new int[]{1});
main.testRunningSum(new int[]{1,2,3,4}, new int[]{1,3,6,10});
main.testRunningSum(new int[]{1,1,1,1,1}, new int[]{1,2,3,4,5});
main.testRunningSum(new int[]{3,1,2,10,1}, new int[]{3,4,6,16,17});
main.testRunningSum(new int[]{-1,1,-1,1}, new int[]{-1,0,-1,0});
```
Note - Above I commented out my empty array test, because the problem said nums.length > 0 in the Constraint

- Run and verify FAILING output (you haven’t implemented runningSum yet!)


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

