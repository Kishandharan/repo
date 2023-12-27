import java.util.ArrayList;
import java.util.List;
public class Duplicate_finding {
    public static void main(String[]args){
        List<Integer>list1 = new ArrayList<>();
        list1.add(1);
        list1.add(2);
        list1.add(3);
        list1.add(4);
        list1.add(5);
        list1.add(6);
        list1.add(7);
        for(int i = 0; i < list1.size(); i++) {
            for(Integer integer : list1) {
                if(list1.get(i) == integer) {
                    System.out.println("There is a duplicate item");
                }
            }
        }
    }
}
