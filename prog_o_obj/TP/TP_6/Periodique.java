package TP.TP_6;

public class Periodique extends Ouvrage {
    private String nom;
    private int numero;
    private String periodicite;

    public Periodique(String nom, int numero, String periodicite) {
        super();
        this.nom = nom;
        this.numero = numero;
        this.periodicite = periodicite;
    }

    public String getNom() { return nom; }
    public int getNumero() { return numero; }
    public String getPeriodicite() { return periodicite; }

    @Override
    public String toString() {
        return "Périodique: " + nom + " (N°" + numero + ", " + periodicite + ") " + super.toString();
    }
}