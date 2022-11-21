/**
 * 
 */
package towerofhanoi;

import java.util.Observable;

/**
 * @author gabel
 * @version 10.18.22
 */
public class HanoiSolver extends Observable {
    private Tower left;
    private Tower right;
    private Tower middle;
    private int numDisks;

    /**
     * Is the hanoiSolver constructor
     * 
     * @param numDisks
     *            The numDisks is supposed to the number of disks that are going
     *            to need to be solved
     */
    public HanoiSolver(int numDisks) {
        this.numDisks = numDisks;
        this.left = new Tower(Position.LEFT);
        this.right = new Tower(Position.RIGHT);
        this.middle = new Tower(Position.MIDDLE);
    }


    /**
     * Is a getter that retrieves the number of disks
     * 
     * @return
     *         The number of disks
     */
    public int disks() {
        return this.numDisks;
    }


    /**
     * getTower is supposed to use a switch statement for different cases of
     * position
     * and tell you based on the position, which tower should the disk be stored
     * in
     * 
     * @param pos
     *            the pos parameter is supposed to be the position from the enum
     *            class
     * @return
     *         is supposed to return the position
     */
    public Tower getTower(Position pos) {
        switch (pos) {
            case LEFT:
                return this.left;

            case MIDDLE:
                return this.middle;

            case RIGHT:
                return this.right;

            default:
                return this.middle;

        }
    }


    /**
     * The toString() method is supposed to create a list of the disks and which
     * tower they
     * occupy.
     * 
     * @return
     *      this.left.toString() + this.middle.toString() + this.right
            .toString();
     */
    public String toString() {

        return this.left.toString() + this.middle.toString() + this.right
            .toString();

    }


    /**
     * The move method is supposed to move the disks by creating a disk, adding
     * the disk to
     * the destination of tower, calls the Observable class to see that the
     * program
     * knows that the disk has changed locations and set the change
     * 
     * @param source
     *            Where the source disk is currently being stored on which
     *            Tower.
     * @param destination
     *            The destination is where the individual disks are supposed to
     *            go.
     */
    private void move(Tower source, Tower destination) {
        Disk n = source.pop();
        destination.push(n);
        this.setChanged();
        notifyObservers(destination.position());

    }


    /**
     * The solve towers is supposed to solve the Hanoi towers for n disks
     * 
     * @param currentDisks
     *            the currentDisks is the number of disks in the tower
     * @param startPole
     *            the startPole is the leftmost pole.
     * @param tempPole
     *            the tempPole is the middle pole, is used to move disks around
     * @param endPole
     *            the endPole is where all the disks should end up.
     */
    public void solveTowers(
        int currentDisks,
        Tower startPole,
        Tower tempPole,
        Tower endPole) {
        // base case is total # of required moves, if done correctly, should be
        // right on the endPole
        // e and with the right pegs in the right places
        /**
         * Base cases are 0, if the the number of disks is 0, can't be moved any
         * place
         */
        if (currentDisks == 0) {
            return;
        }

        /**
         * This is the base case for n disks, and we want only want 1 disk left
         * before we
         * solve the tower, if so, move the start pole to the endpole
         */
        if (currentDisks == 1) {
            move(startPole, endPole);
            return;
        }

        /**
         * remove 1 disk, startPole stays the same, but now tempPole is the
         * middle pole but in
         * the end position, so will move disks to
         */
        solveTowers(currentDisks - 1, startPole, endPole, tempPole);
        move(startPole, endPole);
        solveTowers(currentDisks - 1, tempPole, startPole, endPole);
    }


    /**
     * The solve method is supposed to call the solveTowers() method to solve
     * the towers.
     */
    public void solve() {
        solveTowers(numDisks, this.left, this.middle, this.right);
    }

}
