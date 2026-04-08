package TP.TP_6;

public class Main {
    public static void main(String[] args) {
        // Création de la bibliothèque (tableau de taille 10)
        Bibliotheque maBiblio = new BiblioTab(10);

        // Création de quelques ouvrages
        Livre l1 = new Livre("Victor Hugo", "Les Misérables", "Gallimard");
        Periodique p1 = new Periodique("Le Monde", 24500, "Quotidien");
        CD cd1 = new CD("Dark Side of the Moon", "Pink Floyd");

        // Insertion dans la bibliothèque
        maBiblio.ajouter(l1);
        maBiblio.ajouter(p1);
        maBiblio.ajouter(cd1);

        // Affichage du contenu
        System.out.println("\n--- Contenu initial ---");
        System.out.println(maBiblio.toString());

        // Suppression d'un ouvrage (on suppose que le Périodique a la cote 2)
        maBiblio.supprimer(2);

        // Affichage après suppression
        System.out.println("\n--- Contenu après suppression ---");
        System.out.println(maBiblio.toString());
    }
}