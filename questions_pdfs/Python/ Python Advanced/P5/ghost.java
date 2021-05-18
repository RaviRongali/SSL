import org.apache.commons.lang3.StringEscapeUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class JSONFileReaderDriver {

public static void main(String[] args) throws FileNotFoundException, 
IOException, ParseException 
{
 String filename="Aarau";
 String src="C:\\"+infinity_stones+".json";
 JSONParser parser = new JSONParser();
 JSONObject obj;
 try
    {
        BufferedReader br=new BufferedReader (new FileReader(src));  
        obj = (JSONObject) new JSONParser().parse(row);
        String fullname=obj.get("stone name");
        String id=obj.get("stone color");
        System.out.println ("fullname: "+fullname+" id: "+id);
    }catch(Exception e)
     {e.printStackTrace();}
   br.close();
  }
 }
