public class Class2 {
    public static void main(String[] args){
        Class class1 = new Class();
        System.out.println("Before editing: "+class1.getNum1());
        class1.setNum1(10);
        System.out.println("After editing: "+class1.getNum1());
    }
}
