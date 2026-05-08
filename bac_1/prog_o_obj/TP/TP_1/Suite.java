package TP.TP_1;

public class Suite {
    public static void suiteArithmetique(int depart, int raison, int k) {
        for (int i = 0; i < k; i++) {
            System.out.println(depart + i * raison);
        }
    }

    public static void suiteGeometrique(int depart, int raison, int k) {
        for (int index = 0; index < k; index++) {
            System.out.println(depart * Math.pow(raison, index));
            
        }
    }
    public static void suiteFibonacci(int k) {
        int a = 0, b = 1;
        for (int i = 0; i < k; i++) {
            System.out.println(a);
            int temp = a + b;
            a = b;
            b = temp;
        }
    }

    public static void main(String[] args) {
        suiteArithmetique(-200, 99, 20);
        suiteGeometrique(1, 2, 32);
        suiteFibonacci(20);
    }
}
