import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        br.close();
            
        for (int i=1; i<=n; i++){
            //오른쪽 정렬을 i문 안에 같은 들여쓰기에 두 개의 for문을 넣어서
            //j에 해당하는 for문은 왼쪽 공백을, k는 *을 출력하게 함
            
            //공백의 경우, n번째에서는 공백없이 출력되므로 범위를 n-i로 설정
            for (int j=1; j<=n-i; j++){
                bw.write(" ");
            }
            for (int k=1; k<=i; k++){
                bw.write("*");
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}