package course.os.experiment1;

import java.util.PriorityQueue;
import java.util.Random;

public class PrioritySchedule implements Schedule<PriorityPCB> {

    private final PriorityQueue<PriorityPCB> queue;

    public PrioritySchedule() {
        this.queue = new PriorityQueue<>();
    }

    @Override
    public void add(PriorityPCB p) {
        if (p.getRemainingTime() <= 0) return;
        this.queue.add(p);
    }

    @Override
    public void run() {
        init();
        System.out.println("PrioritySchedule Running:");
        while (!queue.isEmpty()) {
            PriorityPCB p = queue.poll();
            p.run();
            this.add(p);
        }
    }

    public void init() {
        System.out.println("random generate some data");

        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            PriorityPCB p = new PriorityPCB(i, 0, random.nextInt(20), random.nextInt(10));
            add(p);
            System.out.println(p);
        }
    }
}
