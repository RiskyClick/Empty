import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class RobotPathDecoding {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int T = in.nextInt();
        String thorwaway = in.nextLine();
        int rep = 1;
        while(rep <= T){
            String initialString = in.nextLine();
            String decodedString = returnOnlyChars(initialString);
            System.out.println("Case #" + rep + ": " + getPos(decodedString));
            rep++;
        }
    }

    private static String getPos(String decodedString) {
        int col = 1;
        int row = 1;
        int n = 0, s = 0, e = 0, w = 0;
        for(int i = 0; i < decodedString.length(); i++){
            if(decodedString.charAt(i) == 'N'){
                row--;
                if(row == 0) {
                    row = 1000000000;
                }
            } else if(decodedString.charAt(i) == 'S'){
                row++;
                if(row == 1000000001){
                    row = 1;
                }
            } else if(decodedString.charAt(i) == 'E'){
                col++;
                if(col == 1000000001){
                    col = 1;
                }
            } else {
                col--;
                if(col == 0){
                    col = 1000000000;
                }
            }
        }
        return col + " " + row;
    }

    private static String returnOnlyChars(String initialString) {
        String decodedString = "";
        int parans = 0;
        ArrayList<Integer> multiBall = new ArrayList<>();
        for(int i = 0; i < initialString.length(); i++){
            if(Character.isDigit(initialString.charAt(i))){
                multiBall.add(Character.getNumericValue(initialString.charAt(i)));
            } else if(initialString.charAt(i) == '('){
                parans++;
            } else if(initialString.charAt(i) == ')'){
                parans--;
                multiBall.remove(multiBall.size() - 1);
                if(parans == 0){
                    multiBall = new ArrayList<>();
                }
            } else {
                if(multiBall.size() > 0) {
                    int multiply = 1;
                    for (int k = multiBall.size(); k > 0; k--) {
                        multiply *= multiBall.get(k - 1);
                    }
                    while (multiply != 0) {
                        decodedString += initialString.charAt(i);
                        multiply--;
                    }
                } else {
                    decodedString += initialString.charAt(i);
                }
            }
        }
        return decodedString;
    }
}
