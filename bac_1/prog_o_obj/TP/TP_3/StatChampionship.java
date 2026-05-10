package TP.TP_3;

public class StatChampionship {
    FootballScores footballScores;

    public StatChampionship(FootballScores footballScores) {
        this.footballScores = footballScores;
    }
     
    public int getMatchsPlayed(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {
            if (footballScores.scores[e][i] != null) count++;
        }
        return count;
    }
    public int getWins(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {

            if (footballScores.scores[e][i] != null && footballScores.scores[e][i].x > footballScores.scores[e][i].y) count++;
        }
        return count;
    }

    public int getDraws(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {

            if (footballScores.scores[e][i] != null && footballScores.scores[e][i].x == footballScores.scores[e][i].y) count++;
        }
        return count;
    }

    public int getLosses(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {

            if (footballScores.scores[e][i] != null && footballScores.scores[e][i].x < footballScores.scores[e][i].y) count++;
        }
        return count;
    }
    
    public int getGoals(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {

            if (footballScores.scores[e][i] != null) count += footballScores.scores[e][i].x;
        }
        return count;
    }

    public int getConceded(int e) {
        int count = 0;
        for (int i = 0; i < footballScores.scores.length; i++) {

            if (footballScores.scores[e][i] != null) count += footballScores.scores[e][i].y;
        }
        return count;
    }

    public int getDifference(int e) {
        return getGoals(e) - getConceded(e);
    }

    public int getPoints(int e) {
        return (getWins(e) * 3) + getDraws(e);
    }

    public int[] getClassement() {
        int[] classement = new int[footballScores.teams.length];

        for (int i = 0; i < footballScores.teams.length; i++) {
            classement[i] = i;
        }

        for (int i = 0; i < classement.length - 1; i++) {
            for (int j = i + 1; j < classement.length; j++) {
                if (getPoints(classement[j]) > getPoints(classement[i])) {
                    int temp = classement[i];
                    classement[i] = classement[j];
                    classement[j] = temp;
                }
            }
        }
        return classement;
    }
    public void printStat() {
        int[] classement = getClassement();
        for (int i = 0; i < classement.length; i++) {
            int place = classement[i];
            System.out.print(footballScores.teams[place]);
            System.out.print(", ");
            System.out.print("nombre de matchs joués : " + getMatchsPlayed(place));
            System.out.print(", ");          
            System.out.print("nombre de victoires : " + getWins(place));
            System.out.print(", ");
            System.out.print("nombre de matchs nuls : " + getDraws(place));
            System.out.print(", ");    
            System.out.print("nombre de défaites : " + getLosses(place));
            System.out.print(", ");
            System.out.print("nombre de but marqués : " + getGoals(place));            
            System.out.print(", ");
            System.out.print("nombre de but encaissés : " + getConceded(place));
            System.out.print(", ");
            System.out.print("différence de buts : " + getDifference(place));
            System.out.print(", ");
            System.out.println("points  : " + getPoints(place));          
        }

    }

    public static void main(String[] args) {
        String[] teams = {"Anderlecht", "Bruges", "Standard", "La louvière"};
        FootballScores footballScores = new FootballScores(teams);
        footballScores.simulateChampionship();
        StatChampionship test = new StatChampionship(footballScores);
        System.out.println(test.getPoints(0));
        System.out.println(test.getPoints(1));
        System.out.println(test.getPoints(2));
        System.out.println(test.getPoints(3));
        test.printStat();
    }
}
