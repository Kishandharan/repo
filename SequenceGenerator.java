import java.util.Scanner;
import java.util.InputMismatchException;
public class SequenceGenerator {
    public static void main(String[] args){
        try {
            Scanner sc1 = new Scanner(System.in);//Start value
            Scanner sc2 = new Scanner(System.in);//end value
            Scanner sc3 = new Scanner(System.in);//step value
            System.out.print("Enter start value: ");
            int start = sc1.nextInt();
            System.out.print("Enter end value: ");
            int end = sc2.nextInt();
            System.out.print("Enter step value: ");
            int step = sc3.nextInt();
            System.out.print("The sequence is:\n");
            for (int i = start; i <= end; i += step) {
                System.out.println(i);
            }
        }
        catch(InputMismatchException exception){
            System.out.println("Please enter a number.");
        }
     }
  }
