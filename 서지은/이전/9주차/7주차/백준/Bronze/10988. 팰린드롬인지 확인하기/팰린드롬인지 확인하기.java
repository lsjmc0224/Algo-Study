import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String word = br.readLine();
        StringBuilder sb = new StringBuilder(word);
        
        //sb안에 입력받은 단어를 넣고 reverse 해준 뒤 string으로 변환
        String rev = sb.reverse().toString();
        
        if (word.equals(rev)){
            System.out.print(1);
        }
        else System.out.print(0);
        
    }
}