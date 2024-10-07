package Easy.FirstUniqueCharacterinaString;

import java.util.HashMap;

public class Solution {

    public int firstUniqChar(String s) {
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for(char c: s.toCharArray()) {
            hashMap.put(c, hashMap.getOrDefault(c, 0)+1);
        }
        System.out.println(hashMap);
        for(int i=0; i<s.length(); i++) {
            if(hashMap.get(s.charAt(i)) == 1)
                return i;
        }
        return 0;
    }
}
