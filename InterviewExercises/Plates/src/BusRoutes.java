import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class BusRoutes {
    public static void main(String[] args) {

        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int T = in.nextInt();
        int reps = 1;
        while(T != 0){
            int N = in.nextInt();
            int days = in.nextInt();
            int[] routes = new int[N];
            for(int i  = 0; i < N; i++){
                routes[i] = in.nextInt();
            }
            System.out.println("Case #" + reps + ": " + solve(routes, days));
            reps++;
            T--;
        }
    }

    private static int solve(int[] rounds, int days){
        int i = rounds.length;

        while(i > 0){
            if(days % rounds[i - 1] == 0){
                i--;
            } else {
                days--;
            }
        }
        return days;
    }
}
