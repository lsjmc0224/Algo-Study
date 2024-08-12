import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];
        
        //배열 안, n번에 숫자 n을 넣어줌
        for (int i=1; i<=n; i++){
            arr[i] = i;
        }
        //m번동안 두 정수를 입력받으면서 숫자를 서로 바꿔줌
        for (int j=0; j<m; j++){
            st = new StringTokenizer(br.readLine(), " ");
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            //temp변수에 배열 a번 째에 있는 수를 넣어주기
            int temp = arr[a];
            //arr[a]에 arr[b]에 있던 수를 넣어줌
            arr[a] = arr[b];
            //arr[b]에는 앞서 temp에 저장해둔 arr[a]의 값을 넣어줌
            arr[b] = temp;
        }
        //arr[1]부터 arr[n]까지 돌면서 출력
        for (int k=1; k<=n; k++){
            System.out.print(arr[k]+" ");
        }
        
        
    }
}