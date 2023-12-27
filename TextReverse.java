import java.util.Scanner;
public class TextReverse {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a text: ");
        String text = sc.next();
        for (int i = text.length(); true; i--)
        {
            char character = text.charAt(i);
            System.out.print(character);
        }
    }
}
