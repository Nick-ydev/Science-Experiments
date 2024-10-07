package Hard.SumofPrefixScoresofStrings;

import java.util.Arrays;
import java.util.HashMap;

public class Solution {

    public int[] sumPrefixScores(String[] words) {

        HashMap<String, Integer> map = new HashMap<>();
        for(String word: words) {
            int i = 1;
            while(i <= word.length()) {
                map.put(word.substring(0, i), map.getOrDefault(word.substring(0, i), 0) + 1);
                i++;
            }
        }

        //"abc","ab","bc","b"

        int[] result = new int[words.length];

        for(int i=0; i < words.length; i++) {
            System.out.println("word: "+words[i]);
            for(String str: map.keySet()) {
                System.out.println("str: "+str);
                if(words[i].startsWith(str)){
                    result[i]++;
                }
            }
            System.out.println("result: "+Arrays.toString(result));
        }



        System.out.println(map);
        return new int[]{1};
    }
}
