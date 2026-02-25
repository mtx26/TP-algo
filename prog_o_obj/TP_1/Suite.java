package TP_1;

public class Suite {
    public int suiteArithmetique(int depart, int raison, int k){
        return depart + (k-1)*raison;
    }

    public int suiteGeometrique(int depart, int raison, int k){
        return (int) (depart * Math.pow(raison, k-1));
    }

    public int suiteFibonacci(int k){
        if (k == 1 || k == 2) {
            return 1;
        } else {
            return suiteFibonacci(k - 1) + suiteFibonacci(k - 2);
        }
    }


    public void main(String[] args) {
        System.out.println(suiteArithmetique(-200, 99, 20)); 
        System.out.println(suiteGeometrique(1, 2, 32)); 
        System.out.println(suiteFibonacci(20)); 
    }
}

