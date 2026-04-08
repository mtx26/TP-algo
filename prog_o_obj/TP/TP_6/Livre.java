package TP.TP_6;


public class Livre extends Ouvrage {
    private String auteur;
    private String titre;
    private String editeur;

    public Livre(String auteur, String titre, String editeur) {
        super();
        this.auteur = auteur;
        this.titre = titre;
        this.editeur = editeur;
    }

    public String getAuteur() { return auteur; }
    public String getTitre() { return titre; }
    public String getEditeur() { return editeur; }

    @Override
    public String toString() {
        return "Livre: '" + titre + "' par " + auteur + " (Ed. " + editeur + ") " + super.toString();
    }
}
