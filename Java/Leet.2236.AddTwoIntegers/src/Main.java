public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        Main main = new Main();
        main.testSum(0, 0, 0);
        main.testSum(1, 1, 2);
        main.testSum(-1, 1, 0);
        main.testSum(100, 100, 200);
        main.testSum(-100, -100, -200);
    }

    //Call sum, comparing the result with the expected result... printing PASS or FAIL accordingly
    public void testSum(int num1, int num2, int expected)
    {
        int sum = sum(num1, num2);
        if (sum == expected) {
            System.out.println("PASS: Expected " + expected + " and got " + sum);
        }
        else {
            System.out.println("FAIL: Expected " + expected + " and got " + sum);
        }
    }

    public int sum(int num1, int num2) {
        return num1 + num2;
    }
}
