import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String LOCALENTRADA = "arq.txt";

        List<Integer> dados = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(LOCALENTRADA))) {
            String line;
            while ((line = reader.readLine()) != null) {
                dados.add(Integer.parseInt(line));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        List<Long> temposBubble = new ArrayList<>();
        List<Long> temposQuick = new ArrayList<>();
        List<Long> memorias = new ArrayList<>();

        long startTime, endTime, elapsedTime, startMemory, endMemory, usedMemory;

        for (int i = 0; i < 10; i++) {
            startTime = System.nanoTime();
            startMemory = memoryUsed();
            bubbleSort(new ArrayList<>(dados));
            endTime = System.nanoTime();
            endMemory = memoryUsed();
            elapsedTime = endTime - startTime;
            usedMemory = endMemory - startMemory;
            temposBubble.add(elapsedTime);
            memorias.add(usedMemory);
            System.out.println("Tempo BubbleSort: " + elapsedTime + " ns - Memória: " + usedMemory + " bytes");
        }

        for (int i = 0; i < 10; i++) {
            startTime = System.nanoTime();
            startMemory = memoryUsed();
            quickSort(new ArrayList<>(dados));
            endTime = System.nanoTime();
            endMemory = memoryUsed();
            elapsedTime = endTime - startTime;
            usedMemory = endMemory - startMemory;
            temposQuick.add(elapsedTime);
            memorias.add(usedMemory);
            System.out.println("Tempo QuickSort: " + elapsedTime + " ns - Memória: " + usedMemory + " bytes");
        }

        // Ordenar o array
        dados = quickSort(new ArrayList<>(dados));

        System.out.println("Fim");
    }

    private static void bubbleSort(List<Integer> arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr.get(j) > arr.get(j + 1)) {
                    int temp = arr.get(j);
                    arr.set(j, arr.get(j + 1));
                    arr.set(j + 1, temp);
                }
            }
        }
    }

    private static List<Integer> quickSort(List<Integer> arr) {
        if (arr.size() <= 1) {
            return arr;
        } else {
            int pivot = arr.get(0);
            List<Integer> less = new ArrayList<>();
            List<Integer> greater = new ArrayList<>();
            for (int i = 1; i < arr.size(); i++) {
                if (arr.get(i) < pivot) {
                    less.add(arr.get(i));
                } else {
                    greater.add(arr.get(i));
                }
            }
            List<Integer> sorted = new ArrayList<>(quickSort(less));
            sorted.add(pivot);
            sorted.addAll(quickSort(greater));
            return sorted;
        }
    }

    private static long memoryUsed() {
        Runtime runtime = Runtime.getRuntime();
        return runtime.totalMemory() - runtime.freeMemory();
    }
}
