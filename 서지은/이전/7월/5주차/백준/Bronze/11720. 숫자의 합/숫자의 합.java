import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String a = br.readLine();
        int sum = 0;
        
        for (int i=0; i<n; i++){
            sum += a.charAt(i)-'0'; //charAt을 하면 아스키를 반환하기 때문에 -'0' 혹은 -48을 해줘야 한다!
        }
        System.out.print(sum);
    }
}