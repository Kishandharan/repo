import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class Quiz1 {
    public static void takeQuiz(String fname, String str1, int limit)throws Exception{
        File f1 = new File(fname);
        ArrayList<String>questions = new ArrayList<>();
        ArrayList<String>answers = new ArrayList<>();
        String[] arr1 = new String[2];
        int[] arr2 = new int[limit];
        int total = 0,marks = 10;
        Scanner sc1 = new Scanner(f1);
        Scanner sc2 = new Scanner(System.in);
        String response1,s1,s2,info1;
        s1 = str1;s2 = " ?";
        info1 = sc1.nextLine();
        for(int i  = 0; i<limit; i++) {
            info1 = sc1.nextLine();
            arr1 = info1.split(",");
            questions.add(arr1[0]);
            answers.add(arr1[1]);
            System.out.print(s1 + arr1[0] + s2);
            response1 = sc2.nextLine();
            if(response1.equals(arr1[1])) {
                arr2[i] = marks;
            }
            else{
                arr2[i] = 0;
            }
        }
        System.out.print("The marks you have scored is: ");
        for (int i = 0; i < limit; i++) {
            total = total+arr2[i];
            //System.out.print(arr2[i]+" ");
        }
        System.out.println(total);
        System.out.println();
        for(int i = 0; i < limit; i++) {
            if(arr2[i] == 0) {
                System.out.println("Q"+(i+1)+" - "+s1+questions.get(i)+s2);
                System.out.println("A"+(i+1)+" - "+answers.get(i));
                System.out.println();
            }
        }
    }
    public static void main(String[]args)throws Exception{
        int limit  = 3;
        ArrayList<String>topics = new ArrayList<>();
        ArrayList<String>labels = new ArrayList<>();
        File ftopic = new File("topics.txt");
        String s1 = "",info1,fname1;
        String[]arr1 = new String[2];
        String[]arr2 = new String[2];
        Scanner sc1 = new Scanner(System.in);
        Scanner sc2 = new Scanner(ftopic);
        while(sc2.hasNext()){
            info1 = sc2.nextLine();
            arr1 = info1.split(",");
            topics.add(arr1[0]);
            labels.add(arr1[1]);
        }
        for(int i = 0; i < topics.size(); i++) {
            System.out.println(i+" - "+topics.get(i));
        }
        System.out.print("Enter the category: ");
        int choice = sc1.nextInt();
        System.out.println("You have chosen "+topics.get(choice));
        fname1 = "Quiz_"+ topics.get(choice)+".csv";
        takeQuiz(fname1, labels.get(choice),limit);
    }
}
