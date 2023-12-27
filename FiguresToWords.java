import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.FileNotFoundException;
public class FiguresToWords {
    public static String convert20(int number)throws FileNotFoundException
    {
        File f1=new File("D:\\Java and kotlin programs\\words6_en.txt");
        Scanner s1 = new Scanner(f1);
        List<String>words = new ArrayList<>();
        String cont;
        for(int i = 0; i<f1.length(); i++){
            cont = s1.nextLine();
            words.add(cont);
        }
        return words.get(number-1);
    }
    public static void main(String[] args)throws FileNotFoundException{
       String con =  convert20(20);
       System.out.println(con);
    }
}
