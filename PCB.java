package course.os.experiment1;

public class PCB {
    private final int id; // process id
    private int state; // 0 means ready, 1 means running, 2 means finished
    private int remainingTime; // the remaining run time required

    public PCB(int id, int state, int remainingTime) {
        this.id = id;
        this.state = state;
        this.remainingTime = remainingTime;
    }

    public int getId() {
        return id;
    }

    public int getState() {
        return state;
    }

    public void setState(int state) {
        if (state == 0 || state == 1 || state == 2) this.state = state;
        else throw new IllegalArgumentException("state must be 1 or 2 or 3");
    }

    public int getRemainingTime() {
        return remainingTime;
    }

    public void setRemainingTime(int remainingTime) {
        this.remainingTime = remainingTime;
    }

    @Override
    public String toString() {
        return "PCB{" +
                "id=" + id +
                ", state=" + state +
                ", time=" + remainingTime +
                '}';
    }
}

class PriorityPCB extends PCB implements Comparable<PriorityPCB> {

    private int priority; // the priority of the process

    public PriorityPCB(int id, int state, int remainingTime, int priority) {
        super(id, state, remainingTime);
        this.priority = priority;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    @Override
    public String toString() {
        return "PCB{" +
                "id=" + getId() +
                ", state=" + getState() +
                ", time=" + getRemainingTime() +
                ", priority=" + priority +
                '}';
    }

    @Override
    public int compareTo(PriorityPCB other) {
        return Integer.compare(this.priority, other.priority);
    }

    public void run() {
        setState(1); // set running
        System.out.printf("running %s \n", this);
        setRemainingTime(getRemainingTime() - 1);
        setPriority(getPriority() + 3);
        setState(0);
    }
}

class RotatePCB extends PCB {

    private int rotate; // rotate time slices
    private int usedCPUTime; // have used CPU time

    public RotatePCB(int id, int state, int remainingTime, int rotate, int usedCPUTime) {
        super(id, state, remainingTime);
        this.rotate = rotate;
        this.usedCPUTime = usedCPUTime;
    }

    public int getRotate() {
        return rotate;
    }

    public void setRotate(int rotate) {
        this.rotate = rotate;
    }

    public int getUsedCPUTime() {
        return usedCPUTime;
    }

    public void setUsedCPUTime(int usedCPUTime) {
        this.usedCPUTime = usedCPUTime;
    }

    @Override
    public String toString() {
        return "PCB{" +
                "id=" + getId() +
                ", state=" + getState() +
                ", time=" + getRemainingTime() +
                ", rotate=" + +getRotate() +
                ", usedCPUTime=" + +getUsedCPUTime() +
                '}';
    }

    public void run() {
        setState(1); // set running
        System.out.printf("running %s \n", this);
        setRemainingTime(getRemainingTime() - 1);
        usedCPUTime++;
        setState(0);
    }
}