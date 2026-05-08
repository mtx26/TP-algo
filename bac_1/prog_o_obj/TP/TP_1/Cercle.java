package TP.TP_1;

public class Cercle {
    private static final double PI = 3.14159265;
    
    public static double perimetre(double rayon) {
        return 2 * PI * rayon;
    }

    public static double aire(double rayon) {
        return PI * Math.pow(rayon, 2);
    }

    public static void main(String[] args) {
        for (int index = 1; index <= 50; index++) {
            System.err.printf("Périmètre: %.2f, Aire: %.2f%n", perimetre(index), aire(index));
        }
    }
}
