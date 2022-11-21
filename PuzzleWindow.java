/**
 * 
 */
package towerofhanoi;

import cs2.Button;
import java.awt.Color;
import cs2.Shape;
import java.util.Observable;
import java.util.Observer;
import cs2.WindowSide;
import cs2.Window;

/**
 * @author gabel
 * @version 10.18.22
 */
public class PuzzleWindow implements Observer {
    private Shape left;
    private Shape right;
    private Shape middle;
    private HanoiSolver game;
    private Window window;
    public static final int WIDTH_FACTOR = 15;
    public static final int DISK_GAP = 1;
    public static final int DISK_HEIGHT = 5;
    private static final int TOWER_WIDTH = 3;
    private static final int TOWER_HEIGHT = 101;
    private static final Color COLOR = Color.black;

    /**
     * The sleep method is a try catch exception, to pause between disk
     * movements
     */
    private void sleep() {
        try {
            Thread.sleep(500);
        }
        catch (Exception e) {
        }
    }


    /**
     * THe clicked Solve method is supposed to allow the solve button to work
     * 
     * @param button
     *            Creates the solve button for the towers of Hanoi
     */
    @SuppressWarnings("deprecation")
    public void clickedSolve(Button button) {
        button.disable();
        new Thread() {
            public void run() {
                game.solve();
            }
        }.start();
    }


    /**
     * The moveDisk method is supposed to get the currentdisk and its position
     * and then
     * determine the tower, and then set the currentPole
     * 
     * @param position
     */
    private void moveDisk(Position position) {
        Disk currentDisk = game.getTower(position).peek();
        Shape currentPole;
        switch (position) {
            case LEFT:
                currentPole = left;
                break;
            case MIDDLE:
                currentPole = middle;
                break;
            case RIGHT:
                currentPole = right;
                break;
            default:
                currentPole = middle;
                break;
        }

        int y = currentPole.getY() + TOWER_HEIGHT - (game.getTower(position)
            .size() * (DISK_HEIGHT + DISK_GAP)) - DISK_GAP;
        int x = currentPole.getX() - (currentDisk.getWidth() - TOWER_WIDTH) / 2;
        currentDisk.moveTo(x, y);
    }


    /**
     * The PuzzleWindow is supposed to create a gui of the towers of Hanoi
     * problem
     * 
     * @param solver
     *            solver is supposed to call solver and solver the towers of
     *            Hanoi
     */
    public PuzzleWindow(HanoiSolver solver) {
        this.game = solver;
        game.addObserver(this);
        this.window = new Window();
        this.window.setTitle("Tower of Hanoi");

        int xVar = window.getGraphPanelWidth();
        int yVar = window.getGraphPanelHeight();

        this.left = new Shape(xVar / 4, yVar / 2 - TOWER_HEIGHT / 2,
            TOWER_WIDTH, TOWER_HEIGHT, COLOR);
        this.middle = new Shape(xVar / 2, (yVar / 2) - TOWER_HEIGHT / 2,
            TOWER_WIDTH, TOWER_HEIGHT, COLOR);
        this.right = new Shape((xVar / 4) * 3, (yVar / 2) - TOWER_HEIGHT / 2,
            TOWER_WIDTH, TOWER_HEIGHT, COLOR);

        for (int i = this.game.disks(); i > 0; i--) {
            Disk disk = new Disk(i * WIDTH_FACTOR);
            this.game.getTower(Position.LEFT).push(disk);
            this.window.addShape(disk);
            moveDisk(Position.LEFT);
        }

        window.addShape(this.left);
        window.addShape(this.middle);
        window.addShape(this.right);

        Button solve = new Button("Solve");
        window.addButton(solve, WindowSide.NORTH);
        solve.onClick(this, "clickedSolve");

    }


    /**
     * THe update method is supposed to update the postions of the disks
     */
    @Override
    public void update(Observable o, Object arg) {
        // TODO Auto-generated method stub
        if (arg.getClass() == Position.class) {
            Position pos = (Position)arg;
            moveDisk(pos);
            sleep();
        }
    }

}
