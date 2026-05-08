package TP.TP_2;

public class Recursion {
    public static int Factorielle(int n) {
        if (n == 0) {
            return 1;
        }
        return n * Factorielle(n - 1);
    }

    public static int Fibo(int n) {
        if (n <= 1) {
            return 1;
        }
        return Fibo(n - 1) + Fibo(n - 2);
    }
    
    public static void main(String[] args) {
        System.out.println(Recursion.Factorielle(8));
        System.out.println(Recursion.Fibo(7));
    }
}
