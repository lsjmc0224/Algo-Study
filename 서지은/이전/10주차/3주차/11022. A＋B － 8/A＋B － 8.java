import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        
        for (int i=1; i<=t; i++){
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str, " ");
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            System.out.println("Case #"+i+": "+a+" + "+b+" = "+(a+b));
        }
    }
}