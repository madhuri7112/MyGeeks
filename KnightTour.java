
public class KnightTour {
	public static int size = 8;

	public static void main (String[] args) {

	}

	public static Grid[] getNextKNightMoves(Grid currentGrid)
	{
		// (i-1, j+2) (i-2, j+1) (i-1, j-2) (i-2, j-1) (i+1, j+2) (i+2, j+1) (i+1, j-2) (i+2, j-1)
        i = currentGrid.x_cord;        
        j = currentGrid.y_coord;

        int[] possibleSteps  = {i-1, j+2,
          i-2, j+1,
          i-1, j-2,
          i-2, j-1,
          i+1, j+2,
          i+2, j+1,
          i+1, j-2,
          i+2, j-1};

        Grid[] possibleGrids = new Grid[8];
        int possibleGridPointer = 0;
        for (int c=0; c< possibleSteps.lenght; c=c+2) {
            Grid ng = new Grid(possibleSteps[c], possibleSteps[c+1]);
            if (ng.isValidGrid()) {}
        }
	}

	public static void findPath() {

	}
}

public class Grid {
	int x_cord;
	int y_coord;

    public grid(int x, int y) {
        this.x_cord = x;
        this.y_coord = y;
    }

	public boolean isValidGrid(int boardSize) {
		if (x_cord>0 && 
			x_cord<=boardSize && 
			y_coord>0 &&
			y_coord<=boardSize) {
			return true;
		}
	}
}