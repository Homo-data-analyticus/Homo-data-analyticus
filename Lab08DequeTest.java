package deque;

import student.TestCase;

/**
 * Tests for the DLinkedDeque class.
 *
 * @author Gabriel Dell 9064
 * @version 10.10.22
 */
public class Lab08DequeTest extends TestCase {

    private Lab08Deque<String> deque;
    private Lab08Deque<String> deque2;
    private Lab08Deque<String> deque3;
    private Lab08Deque<String> deque4;
    private Lab08Deque<String> deque5;


    /**
     * Creates two brand new, empty sets for each test method.
     */
    public void setUp() {
        deque = new Lab08Deque<String>();
        deque2 = new Lab08Deque<String>();
        deque3 = new Lab08Deque<String>();
        deque4 = new Lab08Deque<String>();
        deque5 = new Lab08Deque<String>();


        deque.addToBack("Gabe");

        deque2.addToFront("Hi");
        deque2.addToBack("my name");
        deque2.addToBack("is slim shady");

        deque4.addToFront("Name");
        
        deque5.addToFront("Hi");
        deque5.addToFront("there cutie");
        deque5.addToFront(":)");
        deque5.addToBack("I really ");
        deque5.addToBack("your cute, uwu");
        deque5.addToBack("I think so my waifu");
    }


    /**
     * Tests the add front method
     */
    public void testAddToFront() {
        assertEquals(deque2.getFront(), "Hi");
    }


    /**
     * Tests the remove front method
     */
    public void testRemoveFront() {
        assertEquals(deque2.removeFront(), "Hi");
        assertEquals(deque4.removeFront(), "Name");
        
        assertEquals(deque5.removeFront(), ":)");
        assertEquals(deque5.size(), 5, 0.01);
}


    /**
     * Tests the remove back method
     */
    public void testRemoveBack() {
        assertEquals(deque2.toString(), "[Hi, my name, is slim shady]");
        assertEquals(deque2.removeBack(), "is slim shady");
        assertEquals(deque2.toString(), "[Hi, my name]");
        assertEquals(deque2.removeBack(), "my name");
        assertEquals(deque2.toString(), "[Hi]");
        assertEquals(deque.removeBack(), "Gabe");
        assertEquals(deque.toString(), "[]");
       
    }


    /**
     * Tests the get front function
     */
    public void testGetFront() {
        assertEquals(deque2.getFront(), "Hi");
        deque.addToFront("Real slim shady");
        assertEquals(deque.getFront(), "Real slim shady");
    }


    /**
     * Tests the getter getBack function
     */
    public void testGetBack() {
        assertEquals(deque2.getBack(), "is slim shady");
        assertNotSame(deque2.getBack(), "Hi");
    }


    /**
     * Tests if isEmpty() method is working
     */
    public void testIsEmpty() {
        assertTrue(deque3.isEmpty());
        assertFalse(deque2.isEmpty());
    }


    /**
     * Tests if clear is working properly for a deque
     */
    public void testClear() {
        // deque3 = new Lab08Deque<String>();
        deque2.clear();
        assertEquals(deque2.size, 0);
        deque2.addToFront(" ");
        assertEquals(deque2.getBack(), deque2.getFront());
    }


    /**
     * Tests the toString() method
     */
    public void testToString() {
        assertEquals(deque2.toString(), "[Hi, my name, is slim shady]");
        assertEquals(deque.toString(), "[Gabe]");
    }


    /**
     * Tests the exception for getFront()
     */
    public void testgetFrontException() {
        Exception exception = null;
        try {
            deque3.getFront();
            fail("getFront() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("getFront() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the getBack() exception
     */
    public void testgetBackException() {
        Exception exception = null;
        try {
            deque3.getBack();
            fail("getBack() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("getBack() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the exception from remove back method
     */
    public void testremoveBackException() {
        Exception exception = null;
        try {
            deque3.removeBack();
            fail("removeBack() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("removeBack() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the EmptyQueueException() of the removeFront() method
     */
    public void testremoveFrontException() {
        Exception exception = null;
        try {
            deque3.removeFront();
            fail("removeFront() is not throwing an exception when it should");
        }
        catch (Exception e) {
            exception = e;
        }
        assertTrue("removeFront() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }
    
    public void testRemoveSecond() 
    {
        assertEquals(deque5.removeSecond(), "there cutie");
    }
    
    public void testRemoveSecondToLast() 
    {
        assertEquals(deque5.removeSecondToLast(), "your cute, uwu");
    }
    
    
    /**
     * Tests the exception for getFront()
     */
    public void testgetSecondException() {
        Exception exception = null;
        try {
            deque3.getSecond();
            fail("getSecond() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("getSecond() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the getBack() exception
     */
    public void testgetSecondBackException() {
        Exception exception = null;
        try {
            deque3.getBackSecond();
            fail("getBackSecond() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("getBackSecond() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the exception from remove back method
     */
    public void testRemoveSecondBackException() {
        Exception exception = null;
        try {
            deque3.removeSecondToLast();
            fail("removeSecondToLast() is not throwing an exception when it should");
        }
        catch (EmptyQueueException e) {
            exception = e;
        }
        assertTrue("removeSecondToLast() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }


    /**
     * Tests the EmptyQueueException() of the removeFront() method
     */
    public void testRemoveSecondFrontException() {
        Exception exception = null;
        try {
            deque3.removeSecond();
            fail("removeSecond() is not throwing an exception when it should");
        }
        catch (Exception e) {
            exception = e;
        }
        assertTrue("removeSecond() is throwing the wrong type of exceptions",
            exception instanceof EmptyQueueException);
    }
    

}
