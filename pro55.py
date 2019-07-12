#a
import java.util.*;

public class Thief {
  static TreeSet<Integer> list=new TreeSet<Integer>();
  public static void main(String[] args) {
    Scanner input=new Scanner(System.in);
    int n=input.nextInt();
    int k=input.nextInt();
    int arr[]=new int[n];
    for(int i=0;i<n;i++){
      arr[i]=input.nextInt();
    }
    find(arr,k,0);
    List<Integer> ans=new ArrayList<Integer>(list);
    for(int i=0;i<ans.size();i++)
    {
        System.out.print(ans.get(i));
      if(i<ans.size()-1)
      {
        System.out.print(" ");
      }
    }
input.close();
  }
  public static void find(int[] arr,int k,int w){
    if(k==0){
      list.add(w);
    }
    else{
      for(int i=0;i<arr.length;i++){
        find(arr,k-1,w+arr[i]);
      }
    }
  }
}
