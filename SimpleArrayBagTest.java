/**
 * 
 */
package game;

import student.TestCase;

/**
 * @author gabel
 * @version 10.02.22
 */
public class SimpleArrayBagTest extends TestCase {
    private SimpleArrayBag bag1;

    /**
     * Is the Setup method for the simple bag array class
     */
    public void setUp() {
        bag1 = new SimpleArrayBag();
        bag1.add("test");
        bag1.add("random");
        bag1.add("yo");
    }


    /**
     * Tests the add method by adding nulls and strings
     */
    public void testAdd() {
        assertFalse(bag1.add(null));

        for (int i = 0; i < 20; i++) {
            bag1.add("A string");
        }
        assertFalse(bag1.add(null));
    }


    /**
     * tests the getter GetCurrentSize method by adding objects and checking it
     * gives back the correct size.
     */
    public void testGetCurrentSize() {
        assertEquals(bag1.getCurrentSize(), 3);
    }


    /**
     * Tests the is empty method by creating a new bag and leaving it empty.
     */
    public void testIsEmpty() {
        SimpleArrayBag bag2 = new SimpleArrayBag();
        assertTrue(bag2.isEmpty());
    }


    /**
     * Tests the pick method by adding a string and seeing if it retrieves the
     * right output.
     */
    public void testPick() {
        SimpleArrayBag bag3 = new SimpleArrayBag();
        assertNull(bag3.pick());
        bag3.add("testing");

        Object string = bag3.pick();
        assertTrue(string.equals("testing"));
    }


    /**
     * Tests the remove method by removing strings from a bag.
     */
    public void testRemove() {
        assertFalse(bag1.remove("testing"));
        assertTrue(bag1.remove("yo"));
    }

}
