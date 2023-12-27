import java.util.Scanner;
import java.util.Random;
public class MindPuzzle {
    public static void main(String[] args){
        int score = 0;
        while(true) {
            Random rand = new Random();
            Scanner sc1 = new Scanner(System.in);
            Scanner sc2 = new Scanner(System.in);
            Scanner sc3 = new Scanner(System.in);
            int random = rand.nextInt(0,10);
            System.out.print("Enter a number(1): ");
            int scanner1 = sc1.nextInt();
            System.out.print("Enter a number(2): ");
            int scanner2 = sc2.nextInt();
            System.out.print("Enter a number(3): ");
            int scanner3 = sc3.nextInt();
            boolean statement1 = scanner1 == random;
            boolean statement2 = scanner2 == random;
            boolean statement3 = scanner3 == random;
            if(statement1|statement2|statement3){
                score++;
                System.out.println("Yes! You won the match");
                System.out.println("Your score: "+score);
            }else{
                System.out.println("Sorry, you lose");
                System.out.println("Your score: "+score);
            }

        }
    }
}
