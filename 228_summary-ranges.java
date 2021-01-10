import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    //注意题目说了，给的是有序数组
    public static void main(String[] args) {
        int[] nums = new int[]{1,2,3,5,7};
        System.out.print(summaryRangesII(nums));
    }
    // 228_summary-ranges.java
    public static List<String> summaryRanges(int[] nums) {
        Arrays.sort(nums);
        List<String> res = new ArrayList<String>();
        int last = nums[0];
        StringBuilder tmp = new StringBuilder(Integer.toString(last));
        int i = 1;
        while(i < nums.length){
            if (nums[i] == last+1){
                while(i < nums.length && nums[i] == last){
                    last = nums[i];
                    i += 1;
                }
                tmp.append("->");
                tmp.append(nums[i]);
                System.out.println(tmp.toString());
                if(i < nums.length){
                    last = nums[i];
                }
            }
            else{
                res.add(tmp.toString());
                last = nums[i];
                tmp = new StringBuilder(Integer.toString(last));
                i += 1;
            }
        }
        res.add(tmp.toString());
        return res;
    }
    public static List<String> summaryRangesII(int[] nums) {
        // Arrays.sort(nums);
        List<String> res = new ArrayList<String>();
        System.out.println("testsetset");
        int i = 0, n = nums.length;
        while (i < n) {
            String str = "";
            str += Integer.toString(nums[i]);
            int j = i + 1;
            while (j < n && nums[j] == nums[j - 1] + 1) j++;
            if (j != i + 1) {
                str += "->";
                str += Integer.toString(nums[j - 1]);
            }
            i = j;
            res.add(str);
        }
        System.out.print(res);
        return res;
    }
}