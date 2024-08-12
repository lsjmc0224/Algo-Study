import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] arr = new int[26];
        
        for(int i=0; i<arr.length; i++){
            arr[i] = -1; //-1로 배열을 전부 초기화해줌
        }
        
        String word = br.readLine();
        
        //왜 여기선 word.length()가 붙지?
        for (int i=0; i<word.length(); i++){
            char ch = word.charAt(i); //단어의 각 자릿수를 돌면서 단어 각각의 알파벳을 ch에 저장해줌
            
            if (arr[ch-'a'] == -1){
                //a를 빼주는 이유는 쉽게 알파벳 소문자부터 돌기 때문임!            
                arr[ch-'a'] = i;  
            }
        }
        //간단히 배열 출력하는 법
        for (int val : arr){
            System.out.print(val + " ");
        }
    }
}