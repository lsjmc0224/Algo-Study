import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        //하단에 str에 저장해줄 것
        String str;
        
        //해당 문제는 입력받는 값이 있을 때 출력,
        //더이상 입력되는 값이 없을 때 출력을 멈추므로
        //str에 입력받는 값이 null일 때 break임
        while ((str=br.readLine())!=null){
            st = new StringTokenizer(str, " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
        
            sb.append(a+b).append("\n");
        }
        System.out.print(sb);
    }
}