package TP.TP_6;

public class BiblioTab extends Bibliotheque {
    private Ouvrage[] catalogue;
    private int nbOuvrages;
    private int capaciteMax;

    public BiblioTab(int capaciteMax) {
        this.capaciteMax = capaciteMax;
        this.catalogue = new Ouvrage[capaciteMax];
        this.nbOuvrages = 0;
    }

    @Override
    public void ajouter(Ouvrage o) {
        if (nbOuvrages < capaciteMax) { // Vérification des bornes
            catalogue[nbOuvrages] = o;
            nbOuvrages++;
            System.out.println("Ouvrage ajouté avec succès.");
        } else {
            System.out.println("Erreur : La bibliothèque est pleine.");
        }
    }

    @Override
    public void supprimer(int cote) { // Suppression prenant en argument la cote [cite: 14]
        for (int i = 0; i < nbOuvrages; i++) {
            if (catalogue[i].getCote() == cote) {
                // Décaler les éléments pour combler le trou
                for (int j = i; j < nbOuvrages - 1; j++) {
                    catalogue[j] = catalogue[j + 1];
                }
                catalogue[nbOuvrages - 1] = null;
                nbOuvrages--;
                System.out.println("Ouvrage de cote " + cote + " supprimé.");
                return;
            }
        }
        System.out.println("Erreur : Aucun ouvrage trouvé avec la cote " + cote);
    }

    @Override
    public String toString() { // Affichant le nombre d'ouvrages, puis chaque ouvrage successivement [cite: 15]
        StringBuilder sb = new StringBuilder();
        sb.append("Bibliothèque (").append(nbOuvrages).append(" ouvrage(s) sur ").append(capaciteMax).append(")\n");
        sb.append("--------------------------------------------------\n");
        for (int i = 0; i < nbOuvrages; i++) {
            sb.append(catalogue[i].toString()).append("\n");
        }
        return sb.toString();
    }
}