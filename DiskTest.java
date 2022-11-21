/**
 * 
 */
package towerofhanoi;

import student.TestCase;

/**
 * @author gabel
 * @version 10.18.22
 */
public class DiskTest extends TestCase {
    private Disk one;
    private Disk oneBig;
    private Disk big;
    private Disk two;
    private Disk three;

    /**
     * Is the setup for the disk class
     */
    public void setUp() {
        one = new Disk(1);
        oneBig = new Disk(3);
        big = new Disk(5);
        two = null;
        three = new Disk(1);
    }


    /**
     * Tests the compare to method
     */
    public void testCompareTo() {
        Exception exception = null;
        try {
            one.compareTo(two);
        }
        catch (Exception e) {
            exception = e;
        }
        assertNotNull(exception);
        assertTrue(exception instanceof IllegalArgumentException);

        assertTrue(one.compareTo(big) < 0);
        assertFalse(one.compareTo(big) > 0);
        assertTrue(big.compareTo(one) > 0);
        assertTrue(oneBig.compareTo(big) < 0);
    }


    /**
     * Tests the to string method
     */
    public void testToString() {
        assertEquals(one.toString(), "1");
        assertEquals(big.toString(), "5");
    }


    /**
     * Tests the equal method from the disk class
     */
    public void testEquals() {
        assertFalse(one.equals(null));
        assertTrue(one.equals(one));
        assertFalse(big.equals(oneBig));
        assertTrue(one.getClass().equals(three.getClass()));
        assertTrue(one.getClass().equals(three.getClass()));
        assertFalse(one.equals("String"));
        assertTrue(one.equals(three));

    }

}
