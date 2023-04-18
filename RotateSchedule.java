package course.os.experiment1;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Random;

public class RotateSchedule implements Schedule<RotatePCB> {
    private final Deque<RotatePCB> queue;

    public RotateSchedule() {
        this.queue = new ArrayDeque<>();
    }

    @Override
    public void add(RotatePCB p) {
        if (p.getRemainingTime() <= 0) return;
        this.queue.add(p);
    }

    @Override
    public void run() {
        init();
        System.out.println("RotateSchedule Running:");
        while (!queue.isEmpty()) {
            RotatePCB p = queue.poll();
            p.run();
            if (p.getRemainingTime() <= 0) continue; // finished
            // unfinished
            if (p.getUsedCPUTime() >= p.getRotate()) {
                p.setUsedCPUTime(0);
                this.add(p);
            } else queue.addFirst(p);
        }
    }

    public void init() {
        System.out.println("random generate some data");

        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            RotatePCB p = new RotatePCB(i, 0, random.nextInt(20), random.nextInt(1, 10), 0);
            add(p);
            System.out.println(p);
        }
    }
}
