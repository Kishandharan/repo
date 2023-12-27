import java.util.*;

public class UniqueWords {
    public static void main(String[] args){
        Set<String>set1 = new HashSet<>();
        List<String>list1 = new ArrayList<>();
        List<String>list2 = new ArrayList<>();
        String s1 = "This is a very very good book I am reading this during the vacation to Simla The book author is Agatha Christie";
        String[] arr1;
        arr1 = s1.split(" ");
        int len1 = arr1.length;
        System.out.println(len1);
        for(int i = 0; i < len1; i++){
            set1.add(arr1[i]);
        }
        list1.addAll(set1);
        list2.addAll(list1);
        Collections.sort(list2);
        System.out.println(set1);
        System.out.println(list1);
        System.out.println(list2);
    }
}
