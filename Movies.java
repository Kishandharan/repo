package pkg1;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Movies {
	public static void main(String[] args) throws FileNotFoundException{
		File f1 = new File("indianmovies.txt");
		Scanner sc1 = new Scanner(f1);
		ArrayList<String>movies = new ArrayList<>();
		sc1.nextLine();		
		// Movie at index 1
		// Year at index 2
		// Language at index 7
		while(sc1.hasNextLine()) {
			String line = sc1.nextLine();
			String movie = line.split(",")[1];
			String year = line.split(",")[2];
			String lang = line.split(",")[7];
			if(year.contains("197") & lang.equals("hindi")) {
				movies.add(movie);				
			}
		}
		System.out.print(movies);
		sc1.close();
	}
}
