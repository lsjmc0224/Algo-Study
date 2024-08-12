import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        while(true){
            //일반의 경우는 while(true)로 넣어준다
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            //입력받은 후, 둘 다 0일 때는 break하고
            if (a==0 & b==0){
                break;
            }
            //아닌 경우에는 strngbuilder에 a+b한 값과 .append를 한 번 더 붙여서 개행해줌
            sb.append((a+b)).append("\n");
        }
        System.out.println(sb);
    }
}