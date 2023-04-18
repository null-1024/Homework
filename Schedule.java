package course.os.experiment1;

public interface Schedule<T> {
    void add(T p);

    void run();
}
