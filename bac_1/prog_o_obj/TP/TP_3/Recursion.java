package TP.TP_3;

public class Recursion {
    public static int Fibo(int n) {
        int[] cache = new int[n+1];
        return Fibo(n, cache);
    }

    public static int Fibo(int n, int[] cache) {
        if (n <= 1) {
            return 1;
        }
        if (cache[n] != 0) {
            return cache[n];
        }

        cache[n] = Fibo(n - 1, cache) + Fibo(n - 2, cache);
        return cache[n];
    }
    
    public static void main(String[] args) {
        System.out.println(Recursion.Fibo(45));
    }
}
