import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class BikeTour {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int T = in.nextInt();
        int reps = 1;
        while(T != 0){
            int[] heights = new int[in.nextInt()];
            for(int i  = 0; i < heights.length; i++){
                heights[i] = in.nextInt();
            }
            System.out.println("Case #" + reps + ": " + solve(heights));
            reps++;
            T--;
        }
    }

    private static int solve(int[] heights) {
        int peaks = 0;
        for(int i = 0; i < heights.length; i++){
            //if its not the first or last item in the list
            if(i != 0 && i != heights.length - 1){
                if(heights[i] > heights[i - 1] && heights[i] > heights[i + 1]){
                    peaks++;
                }
            }
        }
        return peaks;
    }
}
