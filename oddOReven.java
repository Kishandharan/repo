import java.util.Scanner;
public class oddOReven {
    public static String numberCheck(int number){
       if((number%2) == 0){
           return "even";
       }else{
           return "odd";
       }
    }
    public static void main(String[] args){
        Scanner sc1 = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = sc1.nextInt();
        String out = numberCheck(number);
        System.out.println("This number is a "+out+" number");
    }
}
