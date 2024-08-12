import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        
        //하단에 케이스 번호로 i를 출력해야 하므로 0이 아닌, 1부터 t까찌 출력해줘야 함
        for (int i=1; i<=t; i++){
            st = new StringTokenizer(br.readLine(), " ");
            //이렇게 문자열이 합쳐질 경우, bw.write 두 번에 나누어서 작성해주기
            bw.write("Case #"+i+": ");
            bw.write(Integer.parseInt(st.nextToken())
                      +Integer.parseInt(st.nextToken())+"\n");     
        }
        br.close();
        
        bw.flush();
        bw.close();
    }
}