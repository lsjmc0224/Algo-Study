import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        for(int i=1; i<10; i++){
            bw.write(n+" * "+i+" = "+(n*i)+"\n");
        }
        // bw.flush는 남아있는 데이터를 모두 출력하는 것!
        bw.flush();
        bw.close();
    }
}