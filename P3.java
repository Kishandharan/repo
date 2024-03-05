import java.util.ArrayList;

public class P3 {
    ArrayList<String> list1;
    P3(ArrayList<String>list1){this.list1 = list1;}

    public ArrayList<String> getPerms() {
        ArrayList<String>perms = new ArrayList<>();
        perms.add(list1.get(0)+list1.get(1)+list1.get(2));
        perms.add(list1.get(0)+list1.get(2)+list1.get(1));
        perms.add(list1.get(1)+list1.get(2)+list1.get(0));
        perms.add(list1.get(2)+list1.get(1)+list1.get(0));
        perms.add(list1.get(1)+list1.get(0)+list1.get(2));
        perms.add(list1.get(2)+list1.get(0)+list1.get(1));
        return perms;
    }
}
