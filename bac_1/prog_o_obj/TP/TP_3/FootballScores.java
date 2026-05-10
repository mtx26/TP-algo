package TP.TP_3;

public class FootballScores {
    Point[][] scores;
    String[] teams;
    
    public FootballScores(String[] teams) {
        this.scores = new Point[teams.length][teams.length];
        this.teams = teams;
    }

    public int getIndex(String équipe) {
        for (int i = 0; i < teams.length; i++) {
            if (teams[i].equals(équipe)) return i;
        }
        return -1;
    }

    public void setScore(int e1, int e2, Point point) {
        this.scores[e1][e2] = point;
        this.scores[e2][e1] = Point.reversed(point);
    }

    public void simulateMatch(int e1, int e2) {
        Point point = new Point((int)(Math.random() * 6), (int)(Math.random() * 6));
        setScore(e1, e2, point);
    }

    public void simulateChampionship() {
        for (int i = 0; i < scores.length; i++) {
            for (int j = 0; j < scores.length; j++) {
                if (this.scores[i][j] == null) {
                    if (i != j) simulateMatch(i, j);
                }
            }
        }
    }

    public static void main(String[] args) {
        String[] teams = {"Anderlecht", "Bruges", "Standard"};
        FootballScores test = new FootballScores(teams);
        System.out.println(test.getIndex("Anderlecht"));
        test.simulateChampionship();
        System.out.println(test.scores[2][1]);
        System.out.println(test.scores[1][2]);
        System.out.println(test.scores[1][1]);
        System.out.println(test.scores[0][1]);
    }
}
