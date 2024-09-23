package Easy.ExcelSheetColumnTitle;

import java.util.List;

public class Solution {
    public String convertToTitle(int columnNumber) {
        List<String> titles = List.of("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
        StringBuilder result = new StringBuilder();
        while(columnNumber > 0) {
            if(columnNumber % 26 == 0)
                result.append(titles.get(25));
            else
                result.append(titles.get((columnNumber % 26)-1));
            columnNumber--;
            columnNumber /= 26;
        }
        return result.reverse().toString();
    }
}