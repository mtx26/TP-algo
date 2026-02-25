package noa.TP_1;

public class Droites {
    public static int droite(double x1, double y1, double x2 , double y2){
        double a = y1 - y2;
        double b = x2 - x1;
        double c = a * x1 + b * y1;
        System.out.println("La droite passant par (" + x1 + "," + y1 + ") et (" + x2 + "," + y2 + ") a pour équation :");
        System.out.println(a + "x + " + b + "y = " + c);
        return 0;
    }

    public static boolean appartient(double a, double b, double c, double x, double y){
        double resultat = (a * x) + (b * y);
        double epsilon = 1e-9; 
        return Math.abs(resultat - c) < epsilon;
     }

     public void main(String[] args) {
        System.out.println("--- Test de la méthode droite ---");
        droite(0, 0, 2, 2); 
        System.out.println("\n--- Test de la méthode appartient ---");
        boolean estSurDroite = appartient(-2, 2, 0, 5, 5);
        System.out.println("Le point (5,5) appartient-il à -2x + 2y = 0 ? " + estSurDroite);
        
        boolean estSurDroite2 = appartient(-2, 2, 0, 1, 3);
        System.out.println("Le point (1,3) appartient-il à -2x + 2y = 0 ? " + estSurDroite2);
     }
    }

