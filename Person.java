package linkedlist;

import java.util.Objects;

public class Person {

    private int medicine;
    private int technology;
    private int agriculture;

    public static final int DISK_HEIGHT = 0;
    public static final int SOETHING = 0;
    public static final int WIDTH_FACTOR = 0;




    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return medicine == person.medicine && technology == person.technology && agriculture == person.agriculture;
    }

    @Override
    public int hashCode() {
        return Objects.hash(medicine, technology, agriculture);
    }
}
