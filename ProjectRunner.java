/**
 * 
 */
package towerofhanoi;

/**
 * @author gabel
 * @version 10.18.22
 */
public class ProjectRunner {

    /**
     * The method is supposed to set the number of disks, and call the
     * HanoiSolver and
     * PuzzleWindow
     * 
     * @param args
     *            the args parameter is supposed to be the disks
     */
    public static void main(String[] args) {
        int disks = 6;

        if (args.length == 1) {
            disks = Integer.parseInt(args[0]);
        }
        HanoiSolver solve = new HanoiSolver(disks);
        PuzzleWindow puzzle = new PuzzleWindow(solve);
    }

}
