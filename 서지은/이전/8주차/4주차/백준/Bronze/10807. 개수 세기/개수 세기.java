import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        //길이가 n만큼인 int 배열 생성
        int[] arr = new int[n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i=0; i<n; i++){
            //두 번째 줄에서 입력받는 수들은 arr에 0번 주소부터 들어가게 함
            arr[i] = Integer.parseInt(st.nextToken());
        }
        //마지막으로 입력받는 수
        int b = Integer.parseInt(br.readLine());
        
        //이 for문에서 j는 배열의 길이만큼 돌면서 b와 동일한 수를 찾음
        for (int j=0; j<arr.length; j++){
            if (b==arr[j]){
                //맨 위에서 count를 0으로 초기화 한 후,
                //arr[j]에서 b와 일치하는 수가 있을 시 count에 1을 더함
                //이렇게 모든 값을 돌고 나면 빠져나오게 됨
                count++;
            }
        }
        System.out.println(count);
        br.close();

    }
}