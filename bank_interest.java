import java.io.File;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.FileNotFoundException;
public class bank_interest {
    public static void main(String[] args)throws FileNotFoundException{
        double interest1;
        File f1 = new File("C:\\Users\\KRISHNA\\IdeaProjects\\_1\\src\\Interest.csv");
        String[]list1 = null;
        List<String>date1 = new ArrayList<>();
        List<String>date2 = new ArrayList<>();
        List<Integer>credit1 = new ArrayList<>();
        List<Integer>debit1 = new ArrayList<>();
        List<String>details1 = new ArrayList<>();
        List<Double>Total1 = new ArrayList<>();

        DateTimeFormatter dtf1 = DateTimeFormatter.ofPattern("dd-MMM-yyyy");
        LocalDate MyDate1;
        LocalDate MyDate2;
        String MyDate3;
        for(int i =0; i < 62; i++) {
            MyDate1 = LocalDate.of(2023, 7, 1);
            MyDate2 = MyDate1.plusDays(i);
            MyDate3 = MyDate2.format(dtf1);
            date2.add(MyDate3);
        }
        System.out.println(date2);
        Scanner sc = new Scanner(f1);
        String info1 = sc.nextLine();
        for(int i = 0; i < 19; i++){
            list1 = sc.nextLine().split(",");
            date1.add(list1[0]);
            if(list1[1]==""){
                credit1.add(0);
            }else{
                credit1.add(Integer.parseInt(list1[1]));
            }
            if(list1[2]==""){
                debit1.add(0);
            }else{
                debit1.add(Integer.parseInt(list1[2]));
            }
            details1.add(list1[3]);
        }
        String dt1 = "";
        int credit = 0;
        int debit = 0;
        int principal1 = 0;
        int opening1 = 0;
        int position = 0;
        double time1 = 1.0/365, rate1 = 5.0/100;
        for (int i = 0; i < date2.size(); i++) {
            dt1 = date2.get(i);
            if(dt1.equals(date1.get(position))){
                credit=credit1.get(position);
                debit=debit1.get(position);
                position++;
            }else{
                credit = 0;
                debit = 0;
            }

            opening1 = principal1;
            principal1 = opening1+credit-debit;
            interest1 = principal1*time1*rate1;
            System.out.println(date2.get(i)+" - "+interest1);
        }


            }
}