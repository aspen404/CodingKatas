console.log("hello");

var sum = function(num1, num2) {
    return num1 + num2;
};

//Call sum, comparing the result with the expected result... printing PASS or FAIL accordingly
var testSum = function(num1, num2, expected) {
    var result = sum(num1, num2);
    if (result == expected) {
        console.log("PASS: Expected " + expected + " and got " + result);
    }
    else {
        console.log("FAIL: Expected " + expected + " and got " + result);
    }
};

testSum(0, 0, 0);
testSum(1, 1, 2);
testSum(-1, 1, 0);
testSum(100, 100, 200);
testSum(-100, -100, -200);
