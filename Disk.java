/**
 * 
 */
package towerofhanoi;

import cs2.Shape;
import student.TestableRandom;
import java.awt.Color;

/**
 * @author gabel
 * @version 10.18.22
 */
public class Disk extends Shape implements Comparable<Disk> {

    /**
     * The disk constructor is taking a parameter width, calls super, creates a
     * new
     * testable random object and randomly selects a color for the background
     * 
     * @param width
     *            the width parameter is supposed to set the disks dimensions
     */
    public Disk(int width) {
        super(0, 0, width, PuzzleWindow.DISK_HEIGHT);
        TestableRandom n = new TestableRandom();
        Color background = new Color(n.nextInt(256), n.nextInt(256), n.nextInt(
            256));
    }


    /**
     * The compare to method is supposed to show relative sizes of disks and
     * compare them
     * 
     * @param otherDisk
     *            the OtherDisk parameter is supposed to help get the size of a
     *            disk
     */
    @Override
    public int compareTo(Disk otherDisk) {
        if (otherDisk == null) {
            throw new IllegalArgumentException();
        }
        return this.getWidth() - otherDisk.getWidth();
    }


    /**
     * The String toString method is supposed to return the width of an disk
     * object
     * 
     * @return
     *         this.getWidth() + ""
     */
    public String toString() {
        return this.getWidth() + "";
    }


    /**
     * The equals methods is supposed to check whether or not 2 disks are the
     * same or not
     * 
     * @param obj
     *      is an object
     * 
     * @return
     *         false
     * 
     */
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass().equals(this.getClass())) {
            Disk object = (Disk)obj;
            return this.getWidth() == object.getWidth();
        }
        return false;
    }

}
