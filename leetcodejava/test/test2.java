package leetcodejava.test;
// package leetcodejava.test;
import leetcodejava.solu.Solution;
public class test2 {
    public static void main(String[] args) {
        Solution solu = new Solution();
        int[] nums = new int[]{1,2,3,6,7,8,11};
        System.out.print(solu.summaryRanges(nums));
    }
}

/*
一个小教训
因为我装完java后没有设置classpath环境变量，所以java寻找包的路径是系统路径和当前路径
因此在/leetcodejava/test路径下执行test2.java，是找不到/leetcodejava/solu/Solution.java这个包的
而在/目录下就可以，因为当前路径下可以找到

ok
问题解决！
 */