import java.util.Scanner;

public class SeqGen2 {
    public static void main(String[]args){
        Scanner sc1 = new Scanner(System.in);//For starting num
        Scanner sc2 = new Scanner(System.in);//For stepping
        Scanner sc3 = new Scanner(System.in);//For Ending
        System.out.print("Enter a number: ");
        int num1 = sc1.nextInt();
        System.out.print("Enter a number: ");
        int num2 = sc2.nextInt();
        System.out.print("Enter a number: ");
        int num3 = sc3.nextInt();
        for(int i = num1; i<num3; i+=num2){
            System.out.println(i);
        }
    }
}
