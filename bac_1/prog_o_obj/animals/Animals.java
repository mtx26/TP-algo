package animals;
public class Animals {
    private boolean has_c_v;

    public Animals(boolean has_c_v) {
        this.has_c_v = has_c_v;
    }

    public boolean hasVertebralColomn() {
        return has_c_v;
    }

    public void print() {
        if (has_c_v)
            System.out.println("Cet animal a une colonne vertébrale.");
        else
            System.out.println("Cet animal n'a pas de colonne vertébrale.");
    }

    public static void main(String[] args) {
        Animals animal = new Animals(true);
        animal.print();
        // Utilisation de animal.has_c_v si besoin
    }
}

// list des famille etc de annimal a homme : animaux -> vertébrés -> mammifères -> primates -> hominides -> humains