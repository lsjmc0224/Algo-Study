import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //기존처럼 str, " " 이렇게 받지 않고
        //현재 입력을 받지 않았으므로 애초에 tokenizer 에서 readLine을 받아온다
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        //이 문제에는 세 정수의 범위가 10의 12승이라는 제한 범위가 있다
        //int형은 10의 12승에 한참 못미치기 때문에 long 타입을 써줘야 함
        //sum이라는 변수에 long 타입 선언, 0으로 넣어주고
        long sum = 0;
        
        //총 변수가 세 가지 주어지므로 0, 1, 2번째에 숫자 세 개를 각각
        //st.nextToken()으로 입력을 받고 sum에 더해준다
        for (int i=0; i<3; i++){
            sum += Long.parseLong(st.nextToken());
        }
        //그리고 마지막에 프린트!
        System.out.println(sum);
    }
}