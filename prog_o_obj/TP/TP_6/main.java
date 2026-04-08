package TP.TP_6;

public class Main {
    public static void main(String[] args) {
        Bibliotheque maBiblio = new BiblioTab(10);

        Livre l1 = new Livre("Victor Hugo", "Les Misérables", "Gallimard");
        Periodique p1 = new Periodique("Le Monde", 24500, "Quotidien");
        CD cd1 = new CD("Dark Side of the Moon", "Pink Floyd");

        maBiblio.ajouter(l1);
        maBiblio.ajouter(p1);
        maBiblio.ajouter(cd1);

        System.out.println("\n--- Contenu initial ---");
        System.out.println(maBiblio.toString());

        maBiblio.supprimer(2);

        System.out.println("\n--- Contenu après suppression ---");
        System.out.println(maBiblio.toString());
    }
}