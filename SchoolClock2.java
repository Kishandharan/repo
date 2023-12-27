public class SchoolClock2 {
    public static void main(String[]args){
        int minute = 0;
        String time1 = "";
        for(int j = 0; j<12; j++){
            for(int i = 0; i<12; i++){
                time1 = (9+j+":"+String.valueOf(minute+i*5));
                double angle1 = (90-(j*30)) + (i * 30) - (i * 2.5);
                System.out.println(time1+" - "+Math.abs(angle1%360));
            }
            System.out.println();
        }
    }
}
