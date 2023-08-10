import java.util.*;

public class p010 {

  public static void main( String[] args ) {
    System.out.println( sieve( 2000000 ) );
  }


  public static int[] sieve( int n ) {

    List<Integer> all_prime = new ArrayList<>();

    boolean prime[] = new boolean[n + 1];

    for ( int i = 0; i < n + 1 ; i ++ ) {
      prime[i] = true;
    }

    for ( int p = 2; p*p <= n; p++ ) {
      if (prime[p] == true ) {
        for(int i = p*p; i <= n; i += p) {
          prime[i] = false; 
        } 
      }
    }

    for( int i = 2; i <= n; i++ ){

      if(prime[i] ==  true) {
        all_prime.add( i );
      }

    }
    System.out.println( all_prime );
    return new int[0];
  }
}
