import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //불린 값으로 낸 사람과 안 낸 사람을 TF로 구분
        boolean[] arr = new boolean[31];
        
        //n으로 입력받은 정수 값을 arr[n] 주솟값에 넣고 True로 설정
        for (int i=0; i<28; i++){
            int n = Integer.parseInt(br.readLine());
            arr[n] = true;
        }
        
        //만약 arr[j]에 값이 없으면 해당하는 j(출석번호)를 출력
        for (int j=1; j<=30; j++){
            if (!arr[j]) System.out.println(j);
        }
    }
}