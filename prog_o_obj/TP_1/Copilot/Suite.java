package TP_1.Copilot;
public class Suite {

    // 1. Suite arithmétique : chaque terme s'obtient en ajoutant la raison au précédent
    public static void suiteArithmetique(int depart, int raison, int k) {
        System.out.print("Suite arithmétique : ");
        long courant = depart;
        for (int i = 0; i < k; i++) {
            System.out.print(courant + (i < k - 1 ? ", " : ""));
            courant += raison;
        }
        System.out.println(); // Retour à la ligne final
    }

    // 2. Suite géométrique : chaque terme s'obtient en multipliant le précédent par la raison
    public static void suiteGeometrique(int depart, int raison, int k) {
        System.out.print("Suite géométrique : ");
        long courant = depart;
        for (int i = 0; i < k; i++) {
            System.out.print(courant + (i < k - 1 ? ", " : ""));
            courant *= raison;
        }
        System.out.println();
    }

    // 3. Suite de Fibonacci : chaque terme est la somme des deux précédents (1, 1, 2, 3, 5...)
    public static void suiteFibonacci(int k) {
        if (k <= 0) {
            System.out.println("Erreur: k doit être strictement positif.");
            return;
        }
        
        long a = 1;
        long b = 1;
        long resultat = 1;

        if (k > 2) {
            for (int i = 3; i <= k; i++) {
                resultat = a + b;
                a = b;
                b = resultat;
            }
        }
        
        System.out.println("Le " + k + "ème élément de la suite de Fibonacci est : " + resultat);
    }

    public static void main(String[] args) {
        // Appels demandés dans l'énoncé
        suiteArithmetique(-200, 99, 20);
        suiteGeometrique(1, 2, 32);
        suiteFibonacci(20);
    }
}