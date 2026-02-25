package noa.TP_1.Copilot;

public class Cercle {

    // Point 4 : Constante de classe (remplace les constantes locales des points 2 et 3)
    public static final double PI = 3.14159265;

    // Point 2 : Méthode périmètre
    public static double perimetre(double rayon) {
        return 2 * PI * rayon;
    }

    // Point 3 : Méthode aire
    public static double aire(double rayon) {
        return PI * rayon * rayon;
    }

    public static void main(String[] args) {
        // Point 5 : Boucle pour afficher l'aire et le périmètre des cercles de rayon 1 à 50
        System.out.println("Rayon | Périmètre          | Aire");
        System.out.println("-----------------------------------------");
        
        for (int r = 1; r <= 50; r++) {
            // Affichage des résultats. 
            // Note: on utilise des variables temporaires pour plus de clarté
            double p = perimetre(r);
            double a = aire(r);
            System.out.println("  " + r + "   | " + p + " | " + a);
        }
    }
}