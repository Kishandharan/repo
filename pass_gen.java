import java.util.Random;

public class pass_gen {
    public static void main(String[]args){

        String[]list1 = {"10","1","9","6","7","3","0","5"};
        String[]list2 = {"a","b","c","d","e","f","g"};
        String pass_alpha1 = choose(list2);
        String pass_digit1 = choose(list1);
        String final_password1 = pass_alpha1+pass_digit1;
        String pass_alpha2 = choose(list2);
        String pass_digit2 = choose(list1);
        String final_password2 = pass_alpha2+pass_digit2;
        String real_pass = final_password1+final_password2;
        System.out.println(real_pass);

    }
    public static String choose(String[] list1){

        String[] li = list1;
        Random rand = new Random();
        int num = rand.nextInt(0,li.length-1);
        return li[num];

    }
}