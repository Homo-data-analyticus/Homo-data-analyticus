/**
 * 
 */
package game;

/**
 * @author gabel
 * @version 10.02.22
 *          Creates a simple linked bag test class for simple linked bag
 */
public class SimpleLinkedBagTest extends student.TestCase {

    private SimpleLinkedBag bag;

    /**
     * The setUp() method for the test class, creating bags and adding objects
     * to them
     */
    public void setUp() {
        bag = new SimpleLinkedBag();
        bag.add("test");
        bag.add("test 2");
        bag.add("test 3");
    }


    /**
     * Tests the add method, by trying to add a null value.
     */
    public void testAdd() {
        String string = null;
        assertFalse(bag.add(string));
    }


    /**
     * tests the pick method by creating a new bag and returning a null output
     * then tests by adding strings and seeing if the function chooses the right
     * output.
     */
    public void testPick() {
        SimpleLinkedBag bag3 = new SimpleLinkedBag();
        assertNull(bag3.pick());

        bag3.add("test");
        bag3.add("testing");
        Object string = bag3.pick();
        assertTrue(string.equals("test") || string.equals("testing"));

    }


    /**
     * Tests the current size method by just taking a bag already created and
     * returning its size
     */
    public void testGetCurrentSize() {
        assertEquals(bag.getCurrentSize(), 3);
    }


    /**
     * Tests the is empty method by creating a new bag and asserting true that
     * is empty without
     * adding any strings to it.
     */
    public void testIsEmpty() {
        SimpleLinkedBag bag4 = new SimpleLinkedBag();
        assertTrue(bag4.isEmpty());
    }


    /**
     * Tests the remove method by removing a variety of objects
     */
    public void testRemove() {
        assertTrue(bag.remove("test"));
        assertTrue(bag.remove("test 3"));
        assertFalse(bag.remove("Your mom"));
    }
}
