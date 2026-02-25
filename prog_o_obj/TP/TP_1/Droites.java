package TP.TP_1;

public class Droites {
    public static void droite(double x1, double y1, double x2 , double y2) {
        double a = y2 - y1;
        double b = x1 - x2;
        double c = x2 * y1 - x1 * y2;
        System.out.println("a:" + a + "b:" + b + "c:" + c);
    }

    public static boolean appartient(double a, double b, double c, double x, double y) {
        return a * x + b *y + c == 0;
    }

    public static void main(String[] args) {
        droite(2, 3, 4, 1);
        System.out.println(appartient(-2, -2, 10, 4, 2));
    }
}
