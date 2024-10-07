package Easy.FindtheLengthoftheLongestCommonPrefix;

public class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {

        int globalMax = 0;
        for(int firstArr: arr1) {
            int localMax = 0;
            System.out.println("firstArr: "+firstArr);
            String s1 = String.valueOf((Integer)firstArr);
            int k = 0;
            for(int secondArr: arr2) {
                System.out.println("secondArr: "+secondArr);
                String s2 = String.valueOf((Integer)secondArr);
                if(k < s1.length() && k < s2.length()) {
                    System.out.println("s1.charAt(k): "+s1.charAt(k));
                    System.out.println("s2.charAt(k): "+s2.charAt(k));
                    if(s1.charAt(k) == s2.charAt(k)) {
                        k++;
                        localMax++;
                    }
                }
            }
            System.out.println("localMax: "+localMax);
            System.out.println("globalMax: "+globalMax);
            globalMax = Math.max(localMax, globalMax);
        }
        return globalMax++;
    }
}
