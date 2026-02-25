package noa.TP_1.Copilot;

public class Droites {

    // 1. Détermine l'équation de la droite ax + by = c passant par 2 points
    public static void droite(double x1, double y1, double x2, double y2) {
        double a = y1 - y2;
        double b = x2 - x1;
        double c = a * x1 + b * y1;
        
        System.out.println("La droite passant par (" + x1 + "," + y1 + ") et (" + x2 + "," + y2 + ") a pour équation :");
        System.out.println(a + "x + " + b + "y = " + c);
    }

    // 2. Vérifie si un point appartient à la droite
    public static boolean appartient(double a, double b, double c, double x, double y) {
        // On calcule la valeur ax + by
        double resultat = (a * x) + (b * y);
        
        // On vérifie si la différence entre le résultat et 'c' est proche de zéro.
        // C'est la bonne pratique en Java pour comparer des variables de type 'double'.
        double epsilon = 1e-9; 
        return Math.abs(resultat - c) < epsilon;
    }

    public static void main(String[] args) {
        // Exemples pour tester que le code compile et fonctionne correctement
        System.out.println("--- Test de la méthode droite ---");
        droite(0, 0, 2, 2); // Droite d'équation y = x (soit -2x + 2y = 0)
        
        System.out.println("\n--- Test de la méthode appartient ---");
        // On teste avec a=-2, b=2, c=0 et le point x=5, y=5
        boolean estSurDroite = appartient(-2, 2, 0, 5, 5);
        System.out.println("Le point (5,5) appartient-il à -2x + 2y = 0 ? " + estSurDroite);
        
        boolean estSurDroite2 = appartient(-2, 2, 0, 1, 3);
        System.out.println("Le point (1,3) appartient-il à -2x + 2y = 0 ? " + estSurDroite2);
    }
}
