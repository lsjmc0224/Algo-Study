import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        br.close();
        
        for (int i=1; i<=n; i++){
            //반복문 안에 j로 한 번 더 반복문을 넣어줌
            // i는 n까지 도는 동안, j는 이러한 i까지 도는 동안 * 출력
            for (int j=1; j<=i; j++){
                bw.write("*");
            }
        //개행의 경우 newLine으로 첫 번째 for문 안에 넣어준다
        bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}