package animals;


public class Mammals extends Animals {
    private boolean has_hair;
    private boolean is_warm_blooded;
    private boolean has_mammary_glands;
    private boolean has_live_birth;
    private boolean has_lungs;
    private int number_of_legs;
    private boolean has_tail;

    public Mammals(boolean has_hair, boolean is_warm_blooded, boolean has_mammary_glands, boolean has_live_birth,
                   boolean has_lungs, int number_of_legs, boolean has_tail) {
        super(true); // Les mammifères ont une colonne vertébrale
        this.has_hair = has_hair;
        this.is_warm_blooded = is_warm_blooded; 
        this.has_mammary_glands = has_mammary_glands;
        this.has_live_birth = has_live_birth;
        this.has_lungs = has_lungs;
        this.number_of_legs = number_of_legs;
        this.has_tail = has_tail;
    }

    public void print() {
        super.print(); // Affiche les informations de la classe parent (Animals)
        System.out.println("Caractéristiques des mammifères :");
        System.out.println("A des poils : " + has_hair);
        System.out.println("Sang chaud : " + is_warm_blooded);
        System.out.println("A des glandes mammaires : " + has_mammary_glands);
        System.out.println("Naissance vivante : " + has_live_birth);
        System.out.println("A des poumons : " + has_lungs);
        System.out.println("Nombre de pattes : " + number_of_legs);
        System.out.println("A une queue : " + has_tail);
    }
}