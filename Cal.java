public class Cal {
    int result;
    int Cal(int num1, int num2, String mode){
        if((mode == "add")){
            this.result=num1+num2;
        } else if (mode == "sub") {
            if(num1>num2){
                this.result = num1-num2;
            }
            else{
                this.result = num2-num1;
            }
        } else if (mode=="mul") {
            this.result = num1*num2;
        } else if (mode=="div") {
            this.result = num1/num2;
        }
        return result;
    }
}
