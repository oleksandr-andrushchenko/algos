import java.io.*;
import java.util.*;

class Prime {

    // Single method to handle variable number of integers
    public void checkPrime(int... numbers) {
        for (int num : numbers) {
            if (isPrime(num)) {
                System.out.print(num + " ");
            }
        }
        System.out.println();
    }

    // Helper method to check if a number is prime
    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n1 = Integer.parseInt(br.readLine());
        int n2 = Integer.parseInt(br.readLine());
        int n3 = Integer.parseInt(br.readLine());
        int n4 = Integer.parseInt(br.readLine());
        int n5 = Integer.parseInt(br.readLine());

        Prime ob = new Prime();

        ob.checkPrime(n1);
        ob.checkPrime(n1, n2);
        ob.checkPrime(n1, n2, n3);
        ob.checkPrime(n1, n2, n3, n4, n5);
    }
}