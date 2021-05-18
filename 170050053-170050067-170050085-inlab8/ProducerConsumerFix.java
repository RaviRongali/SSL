public class ProducerConsumerFix {
    
    static int totalstock=0;
   
    public static void main(String []args) throws InterruptedException {
 Thread producer=new Thread(){
	public void run(){
        for(int i=0;i<100000;i++){
            totalstock++;
        }
}
    };

    Thread consumer=new Thread(){
public void run(){
        for(int i=0;i<100000;i++){
            totalstock--;
        }
}

    };


    
  
    producer.start();
    
    producer.join();
consumer.start();
    consumer.join();
    System.out.println(totalstock);
    
   }
}
