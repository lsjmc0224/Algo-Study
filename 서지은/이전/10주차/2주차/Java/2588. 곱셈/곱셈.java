import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //int 받을 때 굳이 tokenizer로 안 받고 바로 br.readLine으로 받아도 돌아감
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        
        br.close();
        
        //sb라는 stringbuilder를 생성해주고 그 안에 계산 값을 다 넣어줌
        StringBuilder sb = new StringBuilder();
        
        sb.append(a*(b%10));
        sb.append('\n');
        
        sb.append(a*(b%100/10));
        sb.append('\n');
        
        sb.append(a*(b/100));
        sb.append('\n');
        
        sb.append(a*b);
        //그리고 마지막에 만들어둔 stringbuilder 전체 출력
        System.out.println(sb);
    }
}