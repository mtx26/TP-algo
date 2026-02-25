package animals;

public class primates extends Mammals {
    private boolean has_opposable_thumbs;
    private boolean has_large_brain;
    
    public primates(boolean has_opposable_thumbs, boolean has_large_brain) {
        super(true, true, true, true, true, 4, false);
        this.has_opposable_thumbs = has_opposable_thumbs;
        this.has_large_brain = has_large_brain;
    }

    public void print() {
        super.print(); // Affiche les informations de la classe parent (Mammals)
        System.out.println("Caractéristiques des primates :");
        System.out.println("A des pouces opposables : " + has_opposable_thumbs);
        System.out.println("A un cerveau développé : " + has_large_brain);
    }

    public static void main(String[] args) {
        primates primate = new primates(true, true);
        primate.print();
    }
}
