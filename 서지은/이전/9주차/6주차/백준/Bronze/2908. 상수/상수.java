import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        //입력받은 int 값을 뒤집어주고 string으로 변환해줌 그리고 마지막에 parseInt해준 거
        int a = Integer.parseInt(new StringBuilder(st.nextToken()).reverse().toString());
        int b = Integer.parseInt(new StringBuilder(st.nextToken()).reverse().toString());
        
        System.out.print(a > b ? a:b); //a>b는 조건, 참이면 a출력 거짓이면 b출력
        
    }
}