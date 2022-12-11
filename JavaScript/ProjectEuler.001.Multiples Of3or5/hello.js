console.log("hello");

//calc sum of all multiples of 3 or 5 below target
var calculate = function(target) {
    var sum = 0;
    for (var i = 0; i < target; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            sum = sum + i;
        }
    }
    return sum;
}

//this might be optimized.. we don't need increment by 1... we can count by 3 and then get all the 5s
var calculateOptimized = function(target) {
    var sum = 0;
    //sum all the multiples of 3s
    for (var i = 3; i < target; i+=3)
    {
        sum = sum + i;
    }
    //sum all the multiples of 5, except for the ones we already counted that are also a multiple of 3, like 15
    for (var j = 5; j < target; j+=5)
    {
        if (j % 3 != 0) {
            sum = sum + j;
        }
    }
    return sum;
}

//Call calculate, comparing the result with the expected result.. printing PASS or FAIL accordingly
var testCalculate = function(target, expected) {
    var result = calculate(target);
    console.log((result == expected ? "PASS" : "FAIL") + ": expected " + expected + " got " + result);
}

testCalculate(10, 23);
testCalculate(11, 23+10);
testCalculate(12, 23+10);
testCalculate(13, 23+10+12);
testCalculate(15, 23+10+12);
testCalculate(16, 23+10+12+15);
testCalculate(1000, -1 /*this test will fail - the answer is certainly not negative one - but running it will tell us the answer*/);
