/**
 * 
 */
package towerofhanoi;

import student.TestCase;

/**
 * @author gabel
 * @version 10.18.22
 */
public class TowerTest extends TestCase {
    private Tower one;
    private Tower two;

    /**
     * Creates the setup for the test class
     */
    public void setUp() {
        one = new Tower(Position.LEFT);
        two = new Tower(Position.DEFAULT);
    }


    /**
     * Tests the position of the tower
     */
    public void testPosition() {
        assertEquals(one.position(), Position.LEFT);
        assertEquals(two.position(), Position.DEFAULT);
    }


    /**
     * Tests the push method
     */
    public void testPush() {
        Exception exception = null;
        try {
            one.push(null);
        }
        catch (Exception e) {
            exception = e;
        }
        assertTrue(exception instanceof IllegalArgumentException);

        one.push(new Disk(2));
        two.push(new Disk(4));

        Exception e = null;
        try {
            one.push(new Disk(10));
        }
        catch (Exception e2) {
            e = e2;
        }
        assertTrue(e instanceof IllegalStateException);
    }

}
