public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        testCalculate(10, 23);
        testCalculate(11, 23+10);
        testCalculate(12, 23+10);
        testCalculate(13, 23+10+12);
        testCalculate(15, 23+10+12);
        testCalculate(16, 23+10+12+15);
        testCalculate(1000, -1 /*this test will fail - the answer is certainly not 5 - but running it will tell us the answer*/);

    }

    public static int calculate(int target) {
        var sum = 0;
        for (int i = 0; i < target; i++)
        {
            if (i % 3 == 0 || i % 5 == 0)
            {
                sum += i;
            }
        }
        return sum;
    }

    //Call calculate, comparing the result with the expected result.. printing PASS or FAIL accordingly
    public static void testCalculate(int target, int expected) {
        int result = calculate(target);
        System.out.println((result == expected ? "PASS" : "FAIL") + ": expected " + expected + " got " + result);
    }


}
