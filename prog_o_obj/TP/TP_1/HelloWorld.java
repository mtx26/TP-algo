package TP.TP_1;

public class HelloWorld {

    public static void printHello(String prenom, int age, int taille) {
        System.out.println("Hello World!");
        System.out.println("Mon nom est" + prenom);
        System.out.printf("j'ai %d ans et je mesure %d mètre(s) :-D...", age, taille);
    }

    public static void main(String[] args) {
        printHello("salut", 0, 0);
    }
    
}
