/**
 * 
 */
package arraystack;

import java.util.EmptyStackException;

/**
 * @author gabel
 *
 */
public class ArrayBasedStackTest extends student.TestCase {
    private ArrayBasedStack<String> stack;
    private StackADT<String> stack1;
    private ArrayBasedStack<String> stack2;
    private ArrayBasedStack<String> stack3;
    private ArrayBasedStack<String> stack4;
    private ArrayBasedStack<Integer> stack5;

    public void setUp() {
        stack = new ArrayBasedStack<String>();
        stack1 = new ArrayBasedStack<String>();
        stack2 = new ArrayBasedStack<String>();
        stack3 = new ArrayBasedStack<String>();
        stack4 = new ArrayBasedStack<String>();
        stack5 = new ArrayBasedStack<Integer>();

        for (int j = 0; j < 4; j++) {
            this.stack5.push(j);
        }
    }


    public void testException() {
        Exception thrown = null;
        try {
            // call your method here that will throw the exception
        }
        catch (Exception exception) {
            thrown = exception;
        }

        // checks whether an Exception was actually thrown
        // assertNotNull(thrown);

        // checks whether the right type of Exception was thrown
        assertFalse(thrown instanceof EmptyStackException);
    }


    /**
     * Tests the is empty function to see if the stack contains anything
     */
    public void testIsEmpty() {
        stack.push("bagel");
        assertFalse(stack.isEmpty());
        assertTrue(stack2.isEmpty());

    }


    /**
     * Tests the peek method, to see if it shows the first item in the array
     */
    public void testPeek() {
        stack.push("Dairy Blizzard");
        assertEquals("Dairy Blizzard", stack.peek());

        stack.push("Oreo");
        assertEquals("Oreo", stack.peek());

        Exception thrown = null;
        try {
            this.stack2.peek();
        }
        catch (Exception exception) {
            thrown = exception;
        }
        assertNotNull(thrown);
        assertTrue(thrown instanceof EmptyStackException);
    }


    /**
     * Tests the pop method, to see if it removes the last item inputed.
     */
    public void testPop() {
        stack.push("Pasta");
        stack.push("Meat");
        stack.push("Person");
        assertEquals("Person", stack.pop());
        assertEquals("Meat", stack.pop());
    }


    /**
     * Tests the push method, see's if items can be pushed onto the stack
     */
    public void testPush() {
        stack.push("Pasta");
        assertEquals("Pasta", stack.pop());

        for (int i = 0; i < 10; i++) {
            stack5.push(i);
        }
        assertEquals(stack5.size(), 14, 0.01);
        stack5.push(11);
        assertEquals(stack5.size(), 15, 0.01);
    }


    /**
     * Tests equals method
     */
    public void testEquals() {
        stack1.push("General Tso");
        stack3.push("General Tso");
        stack2.push("Head");

        assertTrue(this.stack1.equals(this.stack1));
        assertFalse(this.stack1.equals(""));
        // If the size() of the stacks are different
        // If the size() of the stacks are same, but the elements are different,
        assertTrue(this.stack3.equals(this.stack1));
        // If the size() of the stacks are same and they have same elements, but
        // the order of the elements are different
        assertFalse(this.stack4.equals(this.stack1));
        // Comparing to an object which is equal, return true
        assertFalse(this.stack1.equals(this.stack2));

        stack4.push(null);
        assertFalse(this.stack4.equals(this.stack3));

    }


    /**
     * Tests the contains methods, see's if the item is contained in the stack
     */
    public void testContains() {
        stack.push("Bitch");
        stack.push("Cock");
        assertTrue(stack.contains("Cock"));
        assertFalse(stack.contains("Bitch slap"));
    }


    /**
     * Tests the size, see's if it gave back the right size
     */
    public void testSize() {
        stack.push("fruit");
        stack.push("vegetable");
        stack.push("meat");
        assertEquals(3, stack.size());
    }


    /**
     * Tests the toString() method
     */
    public void testToString() {
        String strVal = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]";
        String stackVal = stack1.toString();
        assertEquals(strVal, stackVal);
        assertEquals(stack4.toString(), "[]");
        
    }


    /**
     * Tests the clear method, to see if it removes all items
     */
    public void testClear() {
        stack.push("Bagel");
        stack.push("Burger");
        stack.push("Baby");

        assertEquals(stack.size(), 3, 0.01);
        stack.clear();
        assertEquals(stack.size(), 0, 0.01);

    }


    /**
     * Tests the to array method
     */
    public void testToArray() {
        int[] numbers = { 0, 1, 2, 3 };
        Object[] values = stack5.toArray();
        assertEquals(numbers.length, values.length, 0.01);
        for (int i = 0; i < numbers.length; i++) {
            assertEquals(numbers[i], values[i]);
        }
    }

}
