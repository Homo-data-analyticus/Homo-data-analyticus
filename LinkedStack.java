/**
 * 
 */
package towerofhanoi;

import stack.StackInterface;
import java.util.EmptyStackException;

/**
 * @author gabel
 * @version 10.18.22
 * @param <T>
 */
public class LinkedStack<T> implements StackInterface<T> {

    private int size;
    private Node<T> topNode;

    /**
     * Just instantiates the field variables
     * Sets size to 0 and topNode to null
     */
    public LinkedStack() {
        this.topNode = null;
        this.size = 0;
    }


    /**
     * Get the size
     * 
     * @return
     *         returns the size
     */
    public int size() {
        return this.size;
    }


    /**
     * Checks to see if the stack is empty
     * 
     * @return
     *         topNode == null
     */
    public boolean isEmpty() {
        return topNode == null;
    }


    /**
     * Clear method is supposed to clear by setting topNode to null
     * set size to 0
     */
    @Override
    public void clear() {
        this.topNode = null;
        this.size = 0;
    }


    /**
     * The peek method is supposed to show the top stack
     * Throws an emptyStackException() if stack is empty
     */
    @Override
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }

        return this.topNode.getNodeData();
    }


    /**
     * The pop method should take and remove an entry from the last put in
     */
    @Override
    public T pop() {
        if (topNode != null) {
            T data = this.topNode.getNodeData();
            this.topNode = this.topNode.getNextNode();
            size--;
            return data;
        }
        else {
            throw new EmptyStackException();
        }
    }


    /**
     * The push method is supposed to remove an entry by creating a new node
     * setting the next node to topnode and increasing the size
     */
    @Override
    public void push(T anEntry) {
        Node<T> n = new Node<T>(anEntry);
        n.setNextNode(this.topNode);
        Node<T> node = new Node<T>(anEntry, topNode);
        this.topNode = node;
        this.size++;

    }


    /**
     * To string method is supposed to take the entries and put them into a list
     * by
     * using the string builder and toString() methods to convert the entries to
     * strings and
     * appending to the string
     * 
     * @return
     *         string.toString()
     */
    public String toString() {
        StringBuilder string = new StringBuilder();
        string.append("[");
        Node<T> node = topNode;

        while (node != null) {

            if (string.length() > 1) {
                string.append(", ");
            }

            T data = node.getNodeData();
            string.append(data.toString());
            node = node.getNextNode();
        }
        string.append("]");
        return string.toString();
    }

    /**
     * 
     * @author gabel
     *         Private node class, give all the methods to manipulate nodes
     * @param <T>
     *            The parameter<T> is supposed to represent a generic type to
     *            allow different data
     *            types for nodes data and next field variables
     */
    private class Node<T> {
        private T data;
        private Node<T> next;

        /**
         * Node constructor, instantiates data field variable
         * 
         * @param data
         *            data is supposed to hold the data of the the nodes in the
         *            stack
         */
        public Node(T data) {
            this.data = data;
        }


        /**
         * Second Node constructor
         * 
         * @param entry
         *            An entry for the data
         * @param node
         *            Just sets the next node to the argument in Node
         */
        public Node(T entry, Node<T> node) {
            this(entry);
            this.next = node;
        }


        /**
         * setNextNode is supposed to set the next node in the stack
         * 
         * @param node
         *            The node parameter is supposed to be what this.next is.
         */
        public void setNextNode(Node<T> node) {
            this.next = node;
        }


        /**
         * Getter method that retrieves the next node from the setter
         * 
         * @return
         *         Returns the next node
         */
        public Node<T> getNextNode() {
            return this.next;
        }


        /**
         * Another getter method that retrieves the node data
         * 
         * @return
         *         Returns the node data for a specific node
         */
        public T getNodeData()

        {
            return this.data;
        }

    }

}
