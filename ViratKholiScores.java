import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ViratKholiScores {
    public static void main(String[]args){
        ArrayList<Integer>list1 = new ArrayList<>();
        list1.add(100);
        list1.add(132);
        list1.add(167);
        list1.add(195);
        List<Integer>out =
        list1.stream().filter(n -> n > 100).collect(Collectors.toList());
        System.out.println(out);
    }
}
