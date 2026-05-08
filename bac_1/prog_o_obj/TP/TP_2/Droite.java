package TP.TP_2;

public class Droite {
    public double a;
    public double b;
    public double c;

    public Droite(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public String toString() {
        return a + "x" + "+" + b + "y" + "=" + c;
    }

    public boolean isHorizontal() {
        if (this.a == 0 ) {
            return true;
        }
        return false;
    }

    public Point intersection(Droite pt) {
        double D = this.a * pt.b - this.b * pt.a;
        if (D == 0) {
            return null;
        }
        return new Point((this.b * pt.c - pt.b * this.c) / D, (this.c * pt.a - pt.c * this.a) / D);
    }

    public static Droite create(Point p1, Point p2) {
        double a = p2.y - p1.y;
        double b = p1.x - p2.x;
        double c = a * p1.x + b * p1.y;

        return new Droite(a, b, c);
    }

    public static void main(String[] args) {
        Droite d1 = new Droite(0, -5, 4);
        Droite d2 = new Droite(4, 5, 7);
        System.out.println(d1.isHorizontal());
        Point inter = d1.intersection(d2);
        Point p1 = new Point();
        Droite d3 = Droite.create(inter, p1);
        System.err.println(d3);
    }
}
