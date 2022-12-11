public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");

        Main main = new Main();
        //testRunningSum(new int[]{}, new int[]{});
        main.testRunningSum(new int[]{1}, new int[]{1});
        main.testRunningSum(new int[]{1,2,3,4}, new int[]{1,3,6,10});
        main.testRunningSum(new int[]{1,1,1,1,1}, new int[]{1,2,3,4,5});
        main.testRunningSum(new int[]{3,1,2,10,1}, new int[]{3,4,6,16,17});
        main.testRunningSum(new int[]{-1,1,-1,1}, new int[]{-1,0,-1,0});
    }

    //Call runningSum, comparing the result with the expected result.. printing PASS or FAIL accordingly
    public void testRunningSum(int[] nums, int[] expected) {
        int[] retVal = runningSum(nums);

        var pass = true;
        for (int i = 0; i < retVal.length; i++)
        {
            if (retVal[i] != expected[i])
            {
                pass = false;
            }
        }

        if (pass)
        {
            System.out.print("PASS: ");
        }
        else
        {
            System.out.print("FAIL: ");
        }

        System.out.print(" Expected ");
        PrintArray(expected);
        System.out.print(" got ");
        PrintArray(retVal);
        System.out.println("");
    }

    // Convenience method to print out an array
    public void PrintArray(int[] nums) {
        System.out.print("[");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(" " + nums[i] + " ");
        }
        System.out.print("]");
    }

    public int[] runningSum(int[] nums) { return runningSumSecondTry(nums); }

    public int[] runningSumFirstTry(int[] nums) {
        int[] retArray = new int[nums.length];

        int runningSum = 0;
        for (int i = 0; i < nums.length; i++) {
            runningSum = runningSum + nums[i];
            retArray[i] = runningSum;
        }

        return retArray;
    }

    public int[] runningSumSecondTry(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i] + nums[i-1];
        }
        return nums;
    }
}
