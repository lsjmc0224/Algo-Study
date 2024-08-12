import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        double arr[] = new double[Integer.parseInt(br.readLine())];
        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        //배열 안에 입력받은 수 넣기
        for (int i=0; i<arr.length; i++){
            arr[i] = Double.parseDouble(st.nextToken());
        }
        double max = 0;
        Arrays.sort(arr); //배열을 오름차순으로 정렬, 최댓값은 가장 끝에 가게 됨
        
        for (int i=0; i<arr.length; i++){
            //이렇게 다 돌면 가장 끝에 있는 최댓값을 제외하고 그 전까지의 점수들이 한 번씩 다 들어가면서 평균 갈아끼우기
            //arr의 배열에서 arr.length-1의 주솟값에 있는 값이 가장 끝 값...!(왜지?)
            max += ((arr[i] / arr[arr.length-1])*100);
        }   
        //이렇게 갈아끼우기 한 성적들의 평균을 구하는 것이므로 max 값에서 전체 배열 크기(갯수)로 나눠준 뒤 출력하기
        System.out.print(max / arr.length);
    }
}