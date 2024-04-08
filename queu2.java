package pkg1.queue;
import java.util.Queue;
import java.util.LinkedList;

public class queue {

	public static void main(String[] args) {
		Queue<String> queue1 = new LinkedList<>();
	    queue1.offer("Sivashankar");
	    queue1.offer("Suhas");
	    queue1.offer("Shashank");
	    
	   // System.out.println(queue1.isEmpty());
	    
	    //queue1.poll();
	    //queue1.poll();
	    //ueue1.poll();
	    
	    //System.out.println(queue1.isEmpty());
	    //queue1.element();
	    
	    System.out.println(queue1.contains("Suhas"));
	    //System.out.println(queue1.peek());
	}

}
