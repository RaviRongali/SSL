import java.util.Arrays; 
public class Anagrams{
   
     public static void main(String []args){
         
        String s1=args[0];
        String s2=args[1];
        boolean status=true;
        if(s1.length()!=s2.length()){
            status=false;
        }
        else{
        char[] arr1 = s1.toLowerCase().toCharArray();  
        char[] arr2 = s2.toLowerCase().toCharArray();  
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        status = Arrays.equals(arr1,arr2);
        }
        if(status){
           System.out.println("Anagrams");
        }
        else{
        System.out.println("Not Anagrams");
     }
     }
}
