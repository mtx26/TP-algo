package TP.TP_3;

public class ExoCmd {
    public static void main(String[] args) {
        int[] tableau = ExoArray.StringToIntTable(args);

        if (args.length < 2) {
            System.out.println("Il faut au moins 2 paramètres.");
            return;
        }
        System.out.println("Somme : " + ExoArray.Sum(tableau));
        System.out.println("Moyenne : " + ExoArray.Average(tableau));
    }
}
