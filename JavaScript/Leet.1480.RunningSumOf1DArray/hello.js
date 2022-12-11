console.log("hello");

var runningSum = function(nums) {
    //if nums   =   [1, 2,     3,       4]
    //   result =   [1, 2+(1), 3+(2+1), 4+(3+2+1)]
    //which is just   [1, nums[current] + result[current - 1], ...]
    var runningSumResult = [nums[0]];
    for (var i = 1; i < nums.length; i++)
    {
        runningSumResult[i] = nums[i] + runningSumResult[i-1];
    }
    return runningSumResult;
};

//Call runningSum, comparing the result with the expected result.. printing PASS or FAIL accordingly
var testRunningSum = function(nums, expected) {
    var result = runningSum(nums);

    //validate result === expected

    //first confirm they have to be the same length
    var pass = (result.length == expected.length);

    //then compare each element
    for (var i = 0; i < expected.length; i++)
    {
        if (expected[i] != result[i])
        {
            pass = false;
            break;
        }
    }

    console.log((pass ? "PASS":"FAIL") + ": Expected " + expected + " got " + result)
};

testRunningSum([1], [1]);
testRunningSum([1,2,3,4], [1,3,6,10]);
testRunningSum([1,1,1,1], [1,2,3,4]);
testRunningSum([3,1,2,10,1], [3,4,6,16,17]);
testRunningSum([-1,1,-1,1],[-1,0,-1,0]);
