import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        //c의 경우에는 다음 행에서 입력받는 것이므로 readLine을 다시 써줘야 함
        int c = Integer.parseInt(br.readLine());
        
        //c를 60으로 나눈 몫은 a에, 나머지는 b에 더해줌
        a += c/60;
        b += c%60;
        
        if (b>=60){
            a += 1;
            b -= 60;
        }
        if (a>=24){
            a -= 24;
        }
        System.out.println(a + " " + b);
    }
}