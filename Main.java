package course.os.experiment1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("choose schedule: (1 is PrioritySchedule, 2 is RotateSchedule");
        Scanner sc = new Scanner(System.in);
        int choose = sc.nextInt();

        if (choose == 1) new PrioritySchedule().run();
        else if (choose == 2) new RotateSchedule().run();
        else throw new IllegalArgumentException("please choose 1 or 2");
    }
}
