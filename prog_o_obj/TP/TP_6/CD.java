package TP.TP_6;

public class CD extends Ouvrage {
    private String titre;
    private String auteur;

    public CD(String titre, String auteur) {
        super();
        this.titre = titre;
        this.auteur = auteur;
    }

    public String getTitre() { return titre; }
    public String getAuteur() { return auteur; }

    @Override
    public String toString() {
        return "CD: '" + titre + "' par " + auteur + " " + super.toString();
    }
}