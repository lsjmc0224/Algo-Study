import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        
        // 원하는 출력값을 StringBuilder에 저장한 뒤 뽑아내기 위해 사용!
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        //i를 int형이라고 선언 해줘야 함!
        for (int i=0; i<t; i++){
            //for문 안에서 a와 b를 공백을 기준으로 입력받고 돌리기
            st = new StringTokenizer(br.readLine(), " ");
            //위에 선언해준 StringBuilder에 a와 b를 append 해줌
            sb.append(Integer.parseInt(st.nextToken())+Integer.parseInt(st.nextToken()));
            //StringBuilder안에 개행을 추가해줌
            sb.append('\n');
        }
        
        System.out.println(sb);
    }
}