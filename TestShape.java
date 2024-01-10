abstract class Shape{
    public void draw(){
        System.out.println("Draw a shape");
    }
    abstract public void area(int dim1);
}
class Circle extends Shape{
    @Override
    public void draw() {
        System.out.println("Draw a circle");
    }
    public void area(int radius){
        System.out.println(Math.PI * radius * radius);
    }
}

public class TestShape {
    public static void main(String[]args){
        Circle c1 = new Circle();
        c1.draw();
        c1.area(3);
    }
}