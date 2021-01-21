package leetcodejava.solu;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    //注意题目说了，给的是有序数组
    public void main(String[] args) {
        // int[] nums = new int[]{1,2,3,5,7};
        // System.out.print(summaryRangesII(nums));
        System.out.println("hw");;
    }
    // 228_summary-ranges.java
    public List<String> summaryRanges(int[] nums) {
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
    public List<String> summaryRangesII(int[] nums) {
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
    //https://leetcode-cn.com/problems/can-place-flowers/    # no.605
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        //直接贪心算法？
        int flowers = n;
        if(flowers == 0){
            return true;
        }
        if(flowers > (flowerbed.length+1) / 2){
            return false;
        }
        for(int i=0; i<flowerbed.length; i++){
            if(flowers == 0){
                break;
            }
            if(flowerbed[i] == 1){
                continue;
            }
            else{
                // if((i-1 < 0 || flowerbed[i-1] == 0) && (i+1 > flowerbed.length || flowerbed[i+1] == 0)){
                //     flowers--;
                //     flowerbed[i] = 1;
                // }
                // if(i == 0){

                // }
                if(checkOne(flowerbed, i-1) && checkOne(flowerbed, i+1)){
                    flowers --;
                    flowerbed[i] = 1;
                }
            }
        }
        return flowers == 0 ? true : false;
    }
    public boolean checkOne(int[] flowerbed, int i) {
        if(i < 0 || i > flowerbed.length-1){
            return true;
        }
        else{
            return flowerbed[i] == 1 ? false : true;
        }
        // return false;
    }
}