class a{
    public static void m(){
        System.out.println("helllo");
    }
}

class b extends a{
    public void j(){
        super.m();
    }
}
public class Sup {
    public static void main(String[]args){
        b B = new b();
        B.j();
    }
}
