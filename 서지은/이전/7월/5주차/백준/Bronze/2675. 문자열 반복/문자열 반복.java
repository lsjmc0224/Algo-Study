import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int T = Integer.parseInt(br.readLine());
        
        for (int i=0; i<T; i++){
            String[] input = br.readLine().split(" "); //배열 안에서 공백을 기준으로 문자를 쪼갬
            int n = Integer.parseInt(input[0]);
            String S = input[1];
            
            //toCharArray는 string형을 char형으로 바꿔서 정렬해줌
            for (char c : S.toCharArray()){
                //char c 에는 이제 문자가 한 글자씩 쪼개져서 들어가있음.
                //그걸 주솟값 0번부터 n번 반복하는 거임 아래 코드는!
                //예컨대 단어가 new 면 S[0]은 n이고, 이 n을 위에 입력받은 n번만큼 bw에 작성하는 것!
                for (int j=0; j<n; j++){
                    bw.write(c);
                }
            }
            bw.newLine();
        }
        br.close();
        bw.flush();
        bw.close();
    }
}