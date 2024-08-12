import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //정수 하나만 받을 때는 Int 선언 후 그 안에 바로 readline 넣어도 됨
        int a = Integer.parseInt(br.readLine());
        
        if (a>=90) System.out.println("A");
        else if (a>=80) System.out.println("B");
        else if (a>=70) System.out.println("C");
        else if (a>=60) System.out.println("D");
        else System.out.println("F");
        
       
    }
}