import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //위의 st는 한 단락? 에서 밖에 사용을 못하나?
        //n은 입력만 받을 거라 입력만 한 번 받아줌
        Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        //굳이 배열로 만들어서 처리하는 게 아닌, 주어진 값 안에서 max는 가장 작은 값 min은 가장 큰 값으로 초기화 시켜줌
        //이걸 가지고 아래에서 입려되는 값으로 바로 바로 비교할 예정
        int max = -1000001;
        int min = 1000001;
        
        while (st.hasMoreTokens()){
            //val에다가 수를 바로 입력받음
            int val = Integer.parseInt(st.nextToken());
            //만약 입력받은 val값이 Max보다 큰 경우, max에 저장시켜줌
            if (val>max){
                max = val;
            }
            //만약 입력받은 val값이 min보다 작은 경우, min에 저장시켜줌
            if (val<min){
                min = val;
            }
        }
        System.out.println(min + " " + max);
    }
}