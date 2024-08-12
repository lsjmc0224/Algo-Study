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
        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[n];
        
        for (int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            //index value는 늘 고려해줘서 +-1 해주기!
            for (int j=a-1; j<b; j++){
                arr[j] = c;
            }
        }
        //k가 배열을 돌면서 하나씩 뽑아냄
        for (int k=0; k<arr.length; k++){
            bw.write(arr[k]+" ");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}