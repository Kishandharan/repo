import java.util.ArrayList;

public class StreamFiltering {
    public static void main(String args[]){
        ArrayList<Integer>list1 = new ArrayList<>();
        list1.add(10);
        list1.add(12);
        list1.add(86);
        list1.add(98);
        ArrayList<Integer>li = (ArrayList<Integer>) list1.stream().filter(num -> num < 10);
        System.out.println(li);
    }
}
