package arraystack;

import java.util.EmptyStackException;

/**
 * 
 * @author gabel
 *
 * @param <T> of type based for a generic and a stack
 */
public class ArrayBasedStack<T> implements StackADT<T> {
    private T[] stackArray;
    private int size;
    private int capacity;

    /**
     * Public array based stack size
     */
    public ArrayBasedStack() {
        this(100);
    }


    /**
     * Creates an array based stack with the field variables
     * 
     * @param capacity1
     *            capacity should be linked to the capacity field and capacity
     *            when needed
     */
    @SuppressWarnings("unchecked")
    public ArrayBasedStack(int capacity1) {
        this.stackArray = (T[])new Object[capacity1];
        this.size = 0;
        this.capacity = capacity1;
    }


    /**
     * Checks if the stack is empty.
     * 
     * @return Returns true if the stack is empty.
     */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }


    /**
     * Checks the item at the top of the
     * stack without removing it.
     * 
     * @return Item at the top of the stack.
     */
    @Override
    public T peek() {
        if (this.isEmpty()) {
            throw new EmptyStackException();
        }
        return this.stackArray[size - 1];
    }


    /**
     * Removes the item at the top of
     * the stack.
     * 
     * @return The item that was removed.
     */
    @Override
    public T pop() {
        if (this.isEmpty()) {
            throw new EmptyStackException();
        }
        T n = this.stackArray[size - 1];
        this.stackArray[size - 1] = null;
        this.size--;
        return n;
    }


    /**
     * Pushes an item onto the stack.
     * 
     * @param item
     *            Item to be pushed
     *            onto the stack.
     */
    @Override
    public void push(T item) {
        if (item == null) {
            return;
        }
        if (this.size == this.capacity) {
            expandCapacity();
        }
        this.stackArray[size] = item;
        size++;

    }


    /**
     * Expands the capacity of the stack by doubling its current capacity.
     */
    private void expandCapacity() {

        @SuppressWarnings("unchecked")
        T[] newArray = (T[])new Object[this.capacity * 2];

        for (int i = 0; i < this.capacity; i++) {
            newArray[i] = this.stackArray[i];
        }

        this.stackArray = newArray;
        this.capacity *= 2;
    }


    /**
     * Checks if an item is in the stack.
     * 
     * @param item
     *            Item to be looked for.
     * @return Returns true if the item is
     *         somewhere in the stack.
     */
    @Override
    public boolean contains(T item) {
        for (int i = 0; i < this.size; i++) {
            if (item.equals(this.stackArray[i])) {
                return true;
            }
        }
        return false;
    }


    /**
     * Number of items in the stack.
     * 
     * @return The number of items in
     *         the stack.
     */
    @Override
    public int size() {
        return this.size;
    }


    /**
     * Clears the stack (removes all of
     * the items from the stack).
     */
    @Override
    public void clear() {
        T[] array = (T[])new Object[this.capacity];
        this.stackArray = array;
        this.size = 0;

    }


    /**
     * Returns an array with a copy of each element in the stack with the top of
     * the stack being the last element
     *
     * @return the array representation of the stack
     */
    @Override
    public Object[] toArray() {
        @SuppressWarnings("unchecked")
        T[] copy = (T[])new Object[this.size()];
        for (int i = 0; i < this.size(); i++) {
            copy[i] = this.stackArray[i];
        }
        return copy;
    }


    /**
     * Returns the string representation of the stack.
     * 
     * [] (if the stack is empty)
     * [bottom, item, ..., item, top] (if the stack contains items)
     * 
     * @return the string representation of the stack.
     */
    @Override
    public String toString() {
        StringBuilder b = new StringBuilder();
        b.append('[');

        boolean f = true;
        for (int i = 0; i < this.size(); i++) {
            if (!f) {
                b.append(", ");
            }
            else {
                f = false;
            }

            // String.valueOf will print null or the toString of the item
            b.append(String.valueOf(this.stackArray[i]));
        }
        b.append(']');
        return b.toString();
    }


    /**
     * Two stacks are equal iff they both have the same size and contain the
     * same elements in the same order.
     *
     * @param other
     *            the other object to compare to this
     *
     * @return {@code true}, if the stacks are equal; {@code false} otherwise.
     */
    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null) {
            return false;
        }
        if (this.getClass().equals(other.getClass())) {
            ArrayBasedStack<?> otherStack = (ArrayBasedStack<?>)other;
            if (this.size() != otherStack.size()) {
                return false;
            }
            Object[] otherArray = otherStack.toArray();
            for (int i = 0; i < this.size(); i++) {
                if (!(this.stackArray[i].equals(otherArray[i]))) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

}
