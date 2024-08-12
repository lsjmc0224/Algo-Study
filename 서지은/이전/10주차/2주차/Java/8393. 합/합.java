import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        br.close();
        
        //임의 변수 a에 0을 넣어주고
        int a = 0;
        
        //변수 i의 초깃값을 1로, 그리고 n보다 같거나 작을 때까지 a에 1을 더해주며 돌기
        for (int i=1; i<=n; i++) a+=i;
        
        System.out.println(a);
    }
}