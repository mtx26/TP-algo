package TP.TP_6;

import java.time.LocalDate;

public abstract class Ouvrage {
    private static int compteurCote = 1; 
    
    private int cote;
    private LocalDate dateEmprunt; 

    public Ouvrage() {
        this.cote = compteurCote++;
        this.dateEmprunt = null; 
    }

    public int getCote() { return cote; }
    public LocalDate getDateEmprunt() { return dateEmprunt; }
    public void setDateEmprunt(LocalDate dateEmprunt) { this.dateEmprunt = dateEmprunt; }

    @Override
    public String toString() {
        String emprunt = (dateEmprunt == null) ? "Disponible" : "Emprunté le " + dateEmprunt;
        return "[Cote: " + cote + " | Statut: " + emprunt + "]";
    }
}