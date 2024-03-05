import java.util.ArrayList;
public class perm3 {


    public static void main(String[] args){
        ArrayList<String>list1 = new ArrayList<>();
        list1.add("T");
        list1.add("I");
        list1.add("E");
        P3 p3 = new P3(list1);
        System.out.println(p3.getPerms());
    }
}
