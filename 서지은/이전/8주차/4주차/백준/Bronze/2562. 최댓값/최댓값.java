import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int max = 0;
        int index = 0;
        int count = 0;
        int[] arr = new int[9];
        
        for (int i=0; i<9; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        
        //아래의 for 문은 배열 안에 있는 값을 순서대로 순회하는 것
        for (int value : arr) {
            count++;
            
            //순회하면서 count값을 늘려주다가, value값이 max보다 커지고, 저장된 count(index)값이
            //더이상 늘지 않을 때(다 돌았을 때) 빠져나와서 출력!
            if(value>max){
                max = value;
                index = count;
            }
        }
        
        System.out.println(max);
        System.out.println(index);
    }
}