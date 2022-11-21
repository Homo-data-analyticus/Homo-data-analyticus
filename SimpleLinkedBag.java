/**
 * 
 */
package game;

import bag.Node;
import student.TestableRandom;
import bag.SimpleBagInterface;

/**
 * @author gabel
 * @param <T>
 *            The <T> parameter is supposed to of a generic type
 * @version 10.02.22
 *          creates a simple linked bag class
 */
public class SimpleLinkedBag<T> implements SimpleBagInterface<T> {

    private Node<T> firstNode;
    private int numberOfEntries;

    /**
     * Initializes the field variables, firstNode and numberOfEntries.
     */
    public SimpleLinkedBag() {
        this.firstNode = null;
        this.numberOfEntries = 0;
    }


    /**
     * The add method is supposed to see if an entry is null, if so, return
     * false
     * takes the node, sets the node to the firstNode and then add the
     * numberOfEntries and
     * returns true
     */
    @Override
    public boolean add(T anEntry) {
        Node<T> node = new Node<T>(anEntry);

        if (anEntry == null) {
            return false;
        }
        if (isEmpty()) {
            firstNode = node;
            numberOfEntries++;
            return true;

        }

        node.setNext(firstNode);
        firstNode = node;
        numberOfEntries++;
        return true;
    }


    /**
     * The pick method sets currentNode to firstNode, checks if isEmpty() and
     * generates
     * random number to set the size of the bag to and picks a value and is
     * returned.
     * 
     * @return currentNode.getData()
     *         supposed to return the specific index in the bag and return its
     *         data
     */
    public T pick() {
        Node<T> currentNode = firstNode;
        if (isEmpty()) {
            return null;
        }
        TestableRandom random = new TestableRandom();
        int value = random.nextInt(numberOfEntries);
        for (int i = 0; i < value; i++) {
            currentNode = currentNode.getNext();

        }
        return currentNode.getData();

    }


    /**
     * Gets a reference to an entry if it is contained in the bag
     * 
     * @param anEntry
     *            Supposed to be a parameter to check to see if any of the
     *            shapes in the bag
     *            contain an entry
     * @return currentNode
     *         returns the currentNode, which is the index where currentNode =
     *         anEntry
     */
    public Node<T> getReferenceTo(T anEntry) {
        Boolean found = false;
        Node<T> currentNode = firstNode;

        while (!found && (currentNode != null)) {
            if (anEntry.equals(currentNode.getData())) {
                found = true;
            }
            else {
                currentNode = currentNode.getNext();
            }
        }

        return currentNode;
    }


    /**
     * Gets the current size
     */
    @Override
    public int getCurrentSize() {
        return numberOfEntries;
    }


    /**
     * Checks to see if the bag is empty
     */
    @Override
    public boolean isEmpty() {
        return numberOfEntries == 0;
    }


    /**
     * Checks to see if a reference to the entry exists, if so, gets the data
     * from that index
     * in the bag and sets it to localNode, decreases number of entries and
     * returns true once
     * done.
     */
    @Override
    public boolean remove(T anEntry) {
        if (getReferenceTo(anEntry) == null) {
            return false;
        }

        Node<T> localNode = this.getReferenceTo(anEntry);
        localNode.setData(firstNode.getData());
        firstNode = firstNode.getNext();
        numberOfEntries--;
        return true;
    }

}
