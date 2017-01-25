package board.battleship;

import android.os.Build;

/**
 * Created by ericcarboni on 1/24/17.
 */

public class BoardUtil {
    private static final String DEVICE_RPI3 = "rpi3";
    private static String sBoardVariant = "";

    /*
    Return the GPIO pin that the LED is connected on
     */
    public static String getGPIOForLED() {
        switch (getBoardVariant()) {
            case DEVICE_RPI3:
                return "";
            default:
                throw new IllegalStateException("Unknown Build.DEVICE " + Build.DEVICE);
        }
    }

    /*
    Return the GPIO pin that the button is connected on
     */
    public static String getGPIOForButton() {
        switch (getBoardVariant()) {
            case DEVICE_RPI3:
                return "";
            default:
                throw new IllegalStateException("Unknown Build.DEVICE " + Build.DEVICE);
        }
    }

    private static String getBoardVariant() {
        if (!sBoardVariant.isEmpty()) {
            return sBoardVariant;
        }
        sBoardVariant = Build.DEVICE;
        return sBoardVariant;
    }
}
