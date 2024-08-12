import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String word = br.readLine();
        int len = word.length();
        int count = 0;
        
        for (int i=0; i<len; i++){
            char ch = word.charAt(i);
            
            if (ch == 'c' && i<len-1){
                if (word.charAt(i+1) == '=' || word.charAt(i+1) == '-'){
                    i++; //=이나 -에 해당하는 부분까지 뛰어넘기 위해 ++해주는 것
                }
            }
            else if (ch == 'd' && i<len-1){
                if (word.charAt(i+1) == '-'){
                    i++;
                }
                else if (word.charAt(i+1) == 'z' && i<len-2){ //len-1은 맨 끝자리만 참조에서 벗어나지 않게 하기 위함인데
                    //여기서는 세 글자라 ㅣen-2를 해줘야 함
                    if (word.charAt(i+2) == '='){
                        i+=2; //여기는 dz=이므로 두 글자를 뛰어넘어줘야 함
                    }
                }
            }
            else if ((ch == 'l' || ch == 'n')&& i<len-1){
                if (word.charAt(i+1) == 'j'){
                    i++;
                }
            }
            else if (ch == 's' && i<len-1){
                if (word.charAt(i+1) == '='){
                    i++;
                }
            }
            else if (ch == 'z' && i<len-1){
                if (word.charAt(i+1) == '='){
                    i++;
                }
            }
            count++;
        }
        System.out.print(count);
    }
}