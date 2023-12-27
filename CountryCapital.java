import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
public class CountryCapital {
    public static void main(String[] args)throws FileNotFoundException{
        File f1 = new File("Capitals.csv");
        Scanner reader1 = new Scanner(f1);
        String[] list1;
        List<String>countrys = new ArrayList<>();
        List<String>capitals = new ArrayList<>();
        String info1 = reader1.nextLine();
        for (int i = 0; i < 13; i++) {
            list1 = reader1.nextLine().split(",");
            countrys.add(list1[0]);
            capitals.add(list1[1]);
        }
        System.out.print(countrys);
        System.out.println(capitals);
    }
}
