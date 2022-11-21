/**
 * 
 */
package towerofhanoi;

import student.TestCase;

/**
 * @author gabel
 * @version 10.18.22
 */
public class HanoiSolverTest extends TestCase {
    private HanoiSolver one;
    private HanoiSolver two;
    private HanoiSolver three;
    private HanoiSolver four;

    /**
     * The setup method for the hanoi solver class
     */
    public void setUp() {
        one = new HanoiSolver(0);

        two = new HanoiSolver(2);
        two.getTower(Position.LEFT).push(new Disk(2));
        two.getTower(Position.LEFT).push(new Disk(1));

        three = new HanoiSolver(5);
        three.getTower(Position.LEFT).push(new Disk(4));
        three.getTower(Position.LEFT).push(new Disk(3));
        three.getTower(Position.MIDDLE).push(new Disk(2));
        three.getTower(Position.RIGHT).push(new Disk(1));
        three.getTower(Position.RIGHT).push(new Disk(0));

        four = new HanoiSolver(1);
        four.getTower(Position.DEFAULT).push(new Disk(1));
    }


    /**
     * Test method for the number of disks
     */
    public void testDisks() {
        assertEquals(one.disks(), 0, 0.01);
        assertEquals(two.disks(), 2, 0.01);
    }


    /**
     * Tests the get tower method
     */
    public void testGetTower() {
        assertEquals(one.getTower(Position.LEFT).position(), Position.LEFT);
        assertEquals(two.getTower(Position.MIDDLE).position(), Position.MIDDLE);
        assertEquals(three.getTower(Position.RIGHT).position(), Position.RIGHT);
        assertEquals(four.getTower(Position.DEFAULT).position(),
            Position.MIDDLE);
    }


    /**
     * Tests the toString method
     */
    public void testToString() {
        assertEquals(one.toString(), "[][][]");
        assertEquals(three.toString(), "[3, 4][2][0, 1]");
    }


    /**
     * Tests the solve method from the Hanoi solver class
     */
    public void testSolve() {
        assertEquals(one.toString(), "[][][]");
        assertEquals(one.getTower(Position.LEFT).size(), 0, 0.01);
        assertEquals(one.getTower(Position.MIDDLE).size(), 0, 0.01);
        assertEquals(one.getTower(Position.RIGHT).size(), 0, 0.01);
        one.solve();

        assertEquals(one.toString(), "[][][]");
        assertEquals(one.getTower(Position.LEFT).size(), 0, 0.01);
        assertEquals(one.getTower(Position.MIDDLE).size(), 0, 0.01);
        assertEquals(one.getTower(Position.RIGHT).size(), 0, 0.01);

        assertEquals(two.toString(), "[1, 2][][]");
        assertEquals(two.getTower(Position.LEFT).size(), 2, 0.01);
        assertEquals(two.getTower(Position.MIDDLE).size(), 0, 0.01);
        assertEquals(two.getTower(Position.RIGHT).size(), 0, 0.01);
        two.solve();

        assertEquals(two.toString(), "[][][1, 2]");
        assertEquals(two.getTower(Position.LEFT).size(), 0, 0.01);
        assertEquals(two.getTower(Position.MIDDLE).size(), 0, 0.01);
        assertEquals(two.getTower(Position.RIGHT).size(), 2, 0.01);

    }

}
