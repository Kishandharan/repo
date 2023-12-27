import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Filecreater {
    public static void main(String[] args)throws IOException {
        File f1 = new File("Created_By_File_Creater.csv");
        FileWriter fw1 = new FileWriter(f1);
        fw1.write("Hello and welcome");
    }
}
