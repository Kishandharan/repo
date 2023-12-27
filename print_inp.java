import java.util.Scanner;
public class print_inp{
    public static void main(String[] args) {
       Scanner inp = new Scanner(System.in);
       System.out.print("Enter a word: ");
       String input = inp.nextLine();
       System.out.println(input);
       inp.close();
    }
}