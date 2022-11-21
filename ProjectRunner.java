/**
 * 
 */
package game;

/**
 * @author gabel
 * @version 10.02.22
 */
public class ProjectRunner {
    
    /**
     * Is the main center for the gui.
     * @param args
     * the args in this case are the whackAShape() class
     */
    public void main(String[] args) 
    {
        if (args.length > 0) 
        {
            WhackAShape whacker = new WhackAShape(args);
        }
        else 
        {
            WhackAShape whack = new WhackAShape();
        }
    }

}
