import java.util.Scanner;
public class project1 {
    public static void main(String[] args) {
       Scanner Num1 = new Scanner(System.in);
       Scanner Num2 =  new Scanner(System.in);
       System.out.print("Enter num1: ");
       long num1 = Num1.nextLong();
       System.out.print("Enter num2: ");
       long num2 = Num2.nextLong();
       if(num1 < num2){
          System.out.println("The difference is: ");
          System.out.println(num2 - num1);
       }

        if(num1 > num2){
            System.out.print("The difference is: ");
            System.out.println(num1 - num2);
        }

        if(num1 == num2){
            System.out.print("The difference is: ");
            System.out.println(num2 - num1);
        }
    }
}
