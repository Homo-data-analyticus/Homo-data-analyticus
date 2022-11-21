/**
 * 
 */
package towerofhanoi;

import stack.EmptyStackException;
import student.TestCase;

/**
 * @author gabel
 * @version 10.18.22
 */
public class LinkedStackTest extends TestCase {
    private LinkedStack<Integer> one;
    private LinkedStack<Integer> empty;

    /**
     * Tests the setUp method
     */
    public void setUp() {
        one = new LinkedStack<Integer>();
        for (int i = 0; i < 10; i++) {
            one.push(i);
        }
        empty = new LinkedStack<Integer>();
    }


    /**
     * Tests the size
     */
    public void testSize() {
        assertEquals(one.size(), 10);
    }


    /**
     * Tests the isEmpty function
     */
    public void testIsEmpty() {
        assertTrue(empty.isEmpty());
        assertFalse(one.isEmpty());
    }


    /**
     * Tests the clear method
     */
    public void testClear() {
        assertEquals(one.size(), 10, 0.01);
        one.clear();
        assertEquals(one.size(), 0, 0.01);
    }


    /**
     * Tests the peek method
     */
    public void testPeek() {
        assertEquals(one.peek(), 9, 0.01);
        Exception exception = null;
        try {
            empty.peek();
        }
        catch (Exception e) {
            exception = e;
        }
        assertFalse(exception instanceof EmptyStackException);
    }


    /**
     * Tests the pop method
     */
    public void testPop() {
        assertNotNull(one.pop());
        Exception exception = null;
        try {
            empty.pop();
        }
        catch (Exception e) {
            exception = e;
        }
        assertFalse(exception instanceof EmptyStackException);
    }


    /**
     * Tests the push method
     */
    public void testPush() {
        one.push(11);
        assertEquals(one.size(), 11, 0.01);
        assertEquals(one.peek(), 11, 0.01);
    }


    /**
     * Tests the toString method
     */
    public void testToString() {
        assertEquals(one.toString(), "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]");
        assertEquals(empty.toString(), "[]");
    }

}
