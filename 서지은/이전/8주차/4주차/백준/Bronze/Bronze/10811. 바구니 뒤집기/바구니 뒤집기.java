import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[n];
        
        //일차적으로 바구니에 1~n번까지 숫자 부여
        for (int i=0; i<n; i++){
            arr[i] = i+1; //1번에 1이 들어가야 되므로 +1 해줌
        }
        
        //m번 동안의 입력을 받는 동안의 for
        for (int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken())-1; //배열 0부터 시작
            int b = Integer.parseInt(st.nextToken())-1;
            
            //i==j가 아닌 경우 : 역순 정렬해야 할 수가 있는 경우
            while (a < b){
                int temp = arr[a]; //temp에 현재 arr[i]를 넣고
                arr[a] = arr[b];
                arr[b] = temp;
                a++;
                b--; // 자리 바꿔치기 해주고 i에서 더 큰 수, j에서 더 작은 수로 이동하며 숫자 계속 바꿔줌
            }
        }
        
        for (int i=0; i<arr.length; i++)
            System.out.print(arr[i] + " ");
        
        
        br.close();
    }
}