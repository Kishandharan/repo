public class SimpleMath {
    public static void main(String[]args){
        int number1 = 0b0000;
        int number2 = 0b0110;
        int number3 = 0b0001;
        int XOR = number1^number2;
        int SHIFT = number3 << 3;
        float out1 = (float) ((XOR+SHIFT)/0.0001+10-5/100/0b100/0.8096);
        System.out.println(XOR);
        System.out.println(SHIFT);
        System.out.println(out1);
    }
}
