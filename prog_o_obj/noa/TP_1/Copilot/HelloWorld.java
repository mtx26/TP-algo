package noa.TP_1.Copilot;

public class HelloWorld {

    // Point 5 : Méthode printHello prenant en compte les 3 paramètres
    public static void printHello(String prenom, int age, double taille) {
        System.out.println("Hello World!");
        System.out.println("Mon nom est " + prenom + ",");
        System.out.println("j'ai " + age + " ans et je mesure " + taille + " mètre(s) :-D...");
    }

    public static void main(String[] args) {
        // Point 3 : Variables locales (remplacez par vos propres informations)
        String prenom = "Alexandre";
        int age = 25;
        double taille = 1.78;

        // Point 4 : Affichage avec les variables
        System.out.println("--- Mes informations ---");
        System.out.println("Hello World!");
        System.out.println("Mon nom est " + prenom + ",");
        System.out.println("j'ai " + age + " ans et je mesure " + taille + " mètre(s) :-D...");
        System.out.println(); // Ligne vide pour aérer

        // Point 6 : Utilisation de la méthode printHello pour les voisins
        System.out.println("--- Voisin de gauche ---");
        printHello("Sophie", 22, 1.65);
        
        System.out.println();

        System.out.println("--- Voisin de droite ---");
        printHello("Lucas", 26, 1.82);
    }
}