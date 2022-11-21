/**
 * 
 */
package game;

import cs2.Button;
import java.awt.Color;
import bag.SimpleBagInterface;
import cs2.CircleShape;
import cs2.Shape;
import cs2.SquareShape;
import cs2.TextShape;
import cs2.Window;
import cs2.WindowSide;
import student.TestableRandom;

/**
 * @author gabel
 * @version 10.02.22
 */
public class WhackAShape {
    private SimpleBagInterface<Shape> bag;
    private Window window;
    private TestableRandom random;
    private Shape currentShape;
    private Button quitButton;

    /**
     * Creates a whack a shape method with a bag, window and random generator
     * objects
     * creates quitButtons and a strings array in which, a specific string array
     * is added to the
     * bag by random chance.
     */
    public WhackAShape() {
        bag = new SimpleLinkedBag<Shape>();
        window = new Window();
        random = new TestableRandom();

        this.quitButton = new Button("Quit");
        this.quitButton.onClick(this, "clickedQuit");

        window.addButton(quitButton, WindowSide.EAST);
        String[] shapes = { "red circle", "blue circle", "red square",
            "blue square" };

        int bagSize = random.nextInt(6) + 8;
        for (int i = 0; i < bagSize; i++) {
            bag.add(this.buildShape(shapes[random.nextInt(4)]));
        }
        window.addShape(bag.pick());
    }


    /**
     * Tests whether to see if their is a shape to be built onto the screen, if
     * not
     * throws a new run time exception error otherwise adds the shape to the bag
     * 
     * @param string
     *            the string parameter is from a strings array
     */
    public WhackAShape(String[] string) {
        bag = new SimpleLinkedBag<Shape>();
        window = new Window();

        window.setTitle("WhackAShape");

        Button quit = new Button("Quit");
        window.addButton(quit, WindowSide.EAST);
        for (int i = 0; i < string.length; i++) {
            Shape s = null;
            try {
                s = this.buildShape(string[i]);
            }
            catch (RuntimeException e) {
                e.printStackTrace();
            }

            if (s != null) {
                bag.add(s);
            }
        }

        window.addShape(bag.pick());

    }


    /**
     * the build shape method is trying to implement the shapes from the string
     * array
     * and put them on the screen, if the input string doesn't contain specific
     * values
     * will give a illegal argument exception error, otherwise will create the
     * shape.
     * 
     * @param input
     *            the input string is a specific string that is trying to be
     *            created
     * @return
     *         The return argument is the current shape field variable
     */
    private Shape buildShape(String input) {
        TestableRandom generator = new TestableRandom();
        int size = generator.nextInt(101) + 100;
        int x = generator.nextInt(window.getGraphPanelWidth() - size);
        int y = generator.nextInt(window.getGraphPanelHeight() - size);

        Color color;

        if (!input.contains("red") && (!input.contains("blue"))) {
            throw new IllegalArgumentException();
        }
        else if (input.contains("red")) {
            color = Color.red;
        }
        else {
            color = Color.blue;
        }

        if (!input.contains("circle") && (!input.contains("squre"))) {
            throw new IllegalArgumentException();
        }
        else if (input.contains("circle")) {
            this.currentShape = new CircleShape(x, y, size, color);
        }
        else {
            this.currentShape = new SquareShape(x, y, size, color);
        }

        this.currentShape.onClick(this, "clickedShape");
        return this.currentShape;
    }


    /**
     * the clicked shape method is supposed to allow the user to click on the
     * shape and if
     * there aren't any shapes left, then you win.
     * 
     * @param shape
     *            the shape parameter is supposed to be the shape that shows up
     *            on the screen
     */
    public void clickedShape(Shape shape) {
        window.removeShape(shape);
        bag.remove(shape);
        Shape nextShape = bag.pick();
        if (nextShape == null) {
            TextShape winner = new TextShape(window.getGraphPanelWidth(), window
                .getGraphPanelHeight(), "You Win");

            window.addShape(winner);
        }
        else {
            window.addShape(nextShape);
        }

    }


    /**
     * the clicked quit method is supposed show you have no errors in your
     * program
     * 
     * @param button
     *            The button parameter is for the button of clicking exit on the
     *            program
     */
    public void clickedQuit(Button button) {
        System.exit(0);
    }


    /**
     * The get window is supposed get the window
     * 
     * @return
     *         is supposed to return the window
     */
    public Window getWindow() {
        return window;
    }


    /**
     * Supposed to get the bag
     * 
     * @return
     *         Supposed to return the bag
     */
    public SimpleBagInterface<Shape> getBag() {
        return bag;
    }

}
