import java.text.*;
import java.util.*;

 public class Clock implements Runnable{
        public void run(){
        SimpleDateFormat sd = new SimpleDateFormat("HH:mm:ss");
        Date date = new Date();
        sd.setTimeZone(TimeZone.getTimeZone("IST"));
        
        System.out.println(sd.format(date));
        Clock m1=new Clock();  
        Thread t1 =new Thread(m1);
        try{
t1.sleep(1000);
}
        catch (InterruptedException e) {
         System.out.println("Thread " +  t1 + " interrupted.");
      }
        t1.start();
        
        
   
}
    public static void main(String []args){  
    Clock m1=new Clock();  
    Thread t1 =new Thread(m1);  
    t1.start();  
     }  
    } 
