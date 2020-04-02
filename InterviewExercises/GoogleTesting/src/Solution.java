import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.InputMismatchException;
import java.util.Scanner;
import static java.lang.System.exit;
import static java.util.Arrays.sort;

public class Solution {

    private static int[] makeArray(String s){
        //string -> string array -> int array.
        //Converted to int after placing in array now that i dont have to worry about
        //the ints getting too large
        String[] stringArr = s.split(" ");
        int[] intArr = new int[stringArr.length];

        for (int i = 0; i < intArr.length; i++){
            intArr[i] = Integer.parseInt(stringArr[i]);
        }
        return intArr;
    }

    private static int myAlgo(int budget, int[] pc) {

        int houses = 0;

        for(int i = 0; i < pc.length; i++){
            if(budget < pc[i]){
                return houses;
            } else {
                houses++;
                budget -= pc[i];
            }
        }
        return houses;
    }

    public static void main(String[] args) {
        //I made three scanners to keep them from interference
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

        int testCases = 0;
        try {
            testCases = in.nextInt();
        } catch (InputMismatchException e){
            System.out.println(e);
        }

        String toss = in.nextLine();
        //Starts and 1 and ends a <= to keep test numbers in place
        for(int i = 1; i <= testCases; i++){
            //Used strings so that if the numbers get larger then an int
            String second = in.nextLine();
            String third = in.nextLine();
            System.out.println(second);

            //N is size B is budget
            int[] NB = makeArray(second);
            //P is price C is cost
            int[] PC = makeArray(third);

            if(NB.length < 2){
                System.out.println("NB length: " + NB.length);
                exit(0);
            }
            int budget = NB[1];
            //heavy lifting
            sort(PC);

            int totals = myAlgo(budget, PC);
            System.out.println("Case #" + i + ": " + totals);
        }
    }
}
