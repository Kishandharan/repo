import java.io.*;
import java.util.Scanner;
import java.io.FileNotFoundException;
public class addition_using_file_input {
    public static void main(String[] args)throws FileNotFoundException{
        File file1 = new File("D:\\Java programs\\text");
        Scanner f1 = new Scanner(file1);
        String contents = f1.nextLine();
        for(int i = 0; i <= contents.length(); i++)
        {
            contents = f1.nextLine();
            System.out.println(contents);
        }
    }
}
