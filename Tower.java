
/**
 * 
 */
package towerofhanoi;

/**
 * @author gabel
 * @version 10.18.22
 */
public class Tower extends LinkedStack<Disk> {
    private Position position;

    /**
     * The Tower method is supposed to call the super constructor of the linked
     * stack file
     * and setup the field variable position to be used from the enumerator.
     * 
     * @param position
     *            Position of the disks on the screen.
     */
    public Tower(Position position) {
        super();
        this.position = position;
    }


    /**
     * The position method is supposed to just retrieve the current position
     * 
     * @return
     *         returns the position that is currently in the position variable
     */
    public Position position() {
        return this.position;
    }


    /**
     * The push method is supposed to add a disk to the stack, checks if null
     * and if size to
     * throw exceptions, otherwise, calls the super constructor and pushes disk
     * on to the stack
     * if the disk is smaller than the one being compared to it
     */
    @Override
    public void push(Disk disk) {
        if (disk == null) {
            throw new IllegalArgumentException();
        }

        if (this.size() == 0 || disk.compareTo(this.peek()) < 0) {
            super.push(disk);
        }
        else {
            throw new IllegalStateException();
        }

    }

}
