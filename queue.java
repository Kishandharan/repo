package pkg1.queue;
import java.util.LinkedList;
import java.util.Queue;

public class queue {

	public static void main(String[] args) {
		 Queue<String> queue = new LinkedList<String>(); //Create a queue called "queue"
		 queue.offer("Steve");                           //Add a element named "Steve" to the queue
		 queue.offer("John");                            //Add a element named "John" to the queue
		 queue.offer("Villiam");                         //Add a element named "Villiam" to the queue 
		 queue.offer("Robin");                           //Add a element named "Robin" to the queue
		 
		 System.out.println(queue.poll());               //Pop the first element and print it
		 System.out.println(queue.poll());				       //Pop the next element and print it
		 System.out.println(queue.poll());               //Pop the next element and print it
		 System.out.println(queue.poll());               //Pop the next element and print it
		 
		 System.out.println(queue);                      //Print the queue
		                                                 //We already poped the elements so It
		                                                 //will print a empty queue
	}

}
