import java.io.*;
import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CaptionTranslator {
    public static void main(String[] args) throws Exception {
        // Ask user to choose image
        JFileChooser chooser = new JFileChooser();
        chooser.setDialogTitle("Select an Image");
        int result = chooser.showOpenDialog(null);
        if (result != JFileChooser.APPROVE_OPTION) {
            System.out.println("No image selected.");
            return;
        }
        String imagePath = chooser.getSelectedFile().getAbsolutePath();

        // Ask user to choose language
        String[] options = {"French", "Spanish", "German", "Hindi", "Italian"};
        int langChoice = JOptionPane.showOptionDialog(null, "Choose a language", "Language Selection",
                JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);

        if (langChoice == -1) {
            System.out.println("No language selected.");
            return;
        }

        String langCode = String.valueOf(langChoice + 1);  // 1-5

        // Run Python script
        ProcessBuilder pb = new ProcessBuilder(
                "C:\\Users\\ejeev\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
                "caption_translate.py",
                imagePath,
                langCode
        );

        pb.redirectErrorStream(true);
        Process process = pb.start();

        // Output logs
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null)
                System.out.println(line);
        }
    }
}
