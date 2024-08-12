import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        String[] arr = new String[t];
        
        for (int i=0; i<t; i++){
            String st = br.readLine();
            //substring은 문자열을 자르는 도구임!
            //자를문자열.substring(int beginindex, intendindex-1) 마지막에서 -1까지인 거임
            
            //arr[0]은 예제 기준으로 A(사실 0~0주솟값 까지만 가져오겠다는 거) 
            //+ E(st.length-1이 실질적인 마지막, st.length()는 찐막)
            arr[i] = st.substring(0,1) + st.substring(st.length()-1, st.length());
        }
        
        for (int i=0; i<arr.length; i++){
            System.out.println(arr[i]);
        }
    }
}