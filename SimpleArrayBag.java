/**
 * 
 */
package game;

// import bag.Bag;
// import bag.BagInterface;
import bag.SimpleBagInterface;
// import cs2.Shape;
import student.TestableRandom;

/**
 * @author gabel
 * @param <T>
 *      The parameter tag <T> is supposed to represent a generic type
 * @version 10.02.22
 *          Creates a simple bag array class
 */
public class SimpleArrayBag<T> implements SimpleBagInterface<T> {

    private T[] bag;
    private static final int MAX = 18;
    private int numberOfEntries;

    /**
     * Instantiates a simple array bag and sets number of entries to zero.
     */
    public SimpleArrayBag() {
        @SuppressWarnings("unchecked")
        T[] tempbag = (T[])new Object[MAX];
        bag = tempbag;
        numberOfEntries = 0;
    }


    /**
     * The add method, checks for null entries and to see if the number of
     * entries is greater
     * than 18, both conditions if true return false, else a new entry is made
     * for the input
     * argument.
     */
    @Override
    public boolean add(T anEntry) {
        if (anEntry == null) {
            return false;
        }
        if (numberOfEntries >= 18) {
            return false;
        }
        else {
            bag[numberOfEntries] = anEntry;
            numberOfEntries++;
            return true;
        }
    }


    /**
     * The pick method is trying to pull a random shape out of the bag.
     * @return
     *      The return type is supposed to return a specific shape
     */
    public T pick() {
        if (this.isEmpty()) {
            return null;
        }
        TestableRandom random = new TestableRandom();
        int value = random.nextInt(numberOfEntries);
        return bag[value];

    }


    /**
     * This method iterates through a for loop to see if the entries in the bag
     * contain the input
     * argument, if so, it returns that specific index, else returns -1.
     * 
     * @param anEntry
     * @return
     */
    private int getIndexOf(T anEntry) {
        for (int i = 0; i < numberOfEntries; i++) {
            if (bag[i].equals(anEntry)) {
                return i;
            }
        }
        return -1;

    }


    /**
     * Gets the current size of the array bag
     */
    @Override
    public int getCurrentSize() {
        return numberOfEntries;
    }


    /**
     * Gets the number of entries and if it is equal to zero, returns true, else
     * false.
     */
    @Override
    public boolean isEmpty() {
        return numberOfEntries == 0;
    }


    /**
     * The remove method checks to see if the entry is in the bag, if not,
     * return false
     * if so, then get the specific index, take away 1 from the number of
     * entries and return true.
     */
    @Override
    public boolean remove(T anEntry) {
        if (this.getIndexOf(anEntry) == -1) {
            return false;
        }
        bag[getIndexOf(anEntry)] = bag[numberOfEntries - 1];
        bag[numberOfEntries - 1] = null;
        numberOfEntries--;
        return true;
    }
}
