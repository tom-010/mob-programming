import org.junit.Before;
import org.junit.Test;

import java.net.InterfaceAddress;

import static org.junit.Assert.assertEquals;

public class Mob {

    /*
    Feldgröße
    Ameise im Fokus
    Klasse Ameise
    Wo findet die Ameise Zucker?
    Weiss die Ameise, wo sie bereits war?
    Mehrere Zuckerstücke -> Mehrere aufeinander
    Mehrere Zuckerhäufen? -> Zufällig
    Ameise verschwindet nicht
    2D
    Ameise muss wissen, wo Ameisen-Haufen ist
    Planlos umherlaufen?
    Ameise hat: Position
    Vocabs: Ant, Home, Sugar, Field, Movement Strategy
    1. Test: Class Field (Forward, Backwards,...) As Vector

     */

    Ant ant;
    Field field;

    static enum Direction {
        LEFT,
        RIGHT
    }

    class Field {
        public int leftBorder;
        public int rightBorder;

        public Field(int leftBorder, int rightBorder) {
            this.leftBorder = leftBorder;
            this.rightBorder = rightBorder;
        }

        public boolean canMoveTo(int position) {
            return position >= leftBorder&&position <=rightBorder;
        }
    }

    class Ant{

        private int position = 0;
        private Field field;
        private Integer knownSugarPosition = null;
        private MovementProvider movementProvider;

        public Ant(Field field, MovementProvider movementProvider) {
            this.field = field;
            this.movementProvider = movementProvider;
        }

        public Ant(Field field) {
            this(field, new RandomMovementProvider());
        }

        public void move(Direction direction) {
            int desiredPosition =
                    (Direction.RIGHT==direction)?position+1:position-1;
            if(!field.canMoveTo(desiredPosition))
                return;
            position = desiredPosition;
        }

        public int getPosition() {
            return position;
        }

        public void setKnowledgeOfSugar(int sugarPosition) {
            this.knownSugarPosition = sugarPosition;
        }

        public Integer getKnownSugarPosition() {
            return knownSugarPosition;
        }

        public void move() {
            if(getKnownSugarPosition() == null) {
                movementProvider.getNextMove(this.position);
                return;
            }

            if(getKnownSugarPosition() > getPosition()) {
                move(Direction.RIGHT);
            } else {
                move(Direction.LEFT);
            }
        }
    }

    @Before
    public void setUp() throws Exception {
        field = new Field(-100, 100);
        ant = new Ant(field, new MovementProviderSpy());
    }

    @Test
    public void environment() {
    }

    @Test
    public void antCanMoveLeft(){
        ant.move(Direction.LEFT);
        assertEquals(-1, ant.getPosition());
    }

    @Test
    public void antCanMoveLeftTwice() {
        ant.move(Direction.LEFT);
        ant.move(Direction.LEFT);
        assertEquals(-2, ant.getPosition());
    }

    @Test
    public void antCanMoveRight() {
        ant.move(Direction.RIGHT);
        assertEquals(1, ant.getPosition());
    }

    @Test
    public void antCanMoveRightTwice(){
        ant.move(Direction.RIGHT);
        ant.move(Direction.RIGHT);
        assertEquals(2, ant.getPosition());
    }

    @Test
    public void cantCrossLeftBorder() {
        field.leftBorder = 0;
        ant.move(Direction.LEFT);
        assertEquals(0, ant.getPosition());
    }

    @Test
    public void cantCrossRightBorder() {
        field.rightBorder = 0;
        ant.move(Direction.RIGHT);
        assertEquals(0, ant.getPosition());
    }

    @Test
    public void movesTowardsRightSugarWithKnowledge() {
        ant.setKnowledgeOfSugar(50);
        ant.move();
        assertEquals(1, ant.getPosition());
    }

    @Test
    public void movesTowardsLeftSugarWithKnowledge() {
        ant.setKnowledgeOfSugar(-50);
        ant.move();
        assertEquals(-1, ant.getPosition());
    }

    interface MovementProvider {
        Direction getNextMove(int currentPosition);
    }

    class RandomMovementProvider implements MovementProvider {

        @Override
        public Direction getNextMove(int currentPosition) {
            return Direction.LEFT;
        }
    }

    class AiMp implements MovementProvider {

        @Override
        public Direction getNextMove(int currentPosition) {
            // Logik
            return Direction.RIGHT;
        }
    }

    class MovementProviderSpy implements MovementProvider {

        public boolean wasCalled = false;

        @Override
        public Direction getNextMove(int currentPosition) {
            wasCalled = true;
            return Direction.LEFT;
        }
    };

    @Test
    public void ifNoSugarPositionIsKnownAskMovementProvider(){
        MovementProviderSpy mp = new MovementProviderSpy();
        Ant ant = new Ant(field, mp);
        ant.move();
        assertEquals(true, mp.wasCalled);
    }
}