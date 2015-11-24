import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class PE4 {
  private static final int MAX_NUM = 9999;
  private static final int MIN_NUM = 100;

  public static void main(String[] args) {
    doTest();
    doProblem();
  }

  private static void doTest() {
    verifyPalindrome(0, true);
    verifyPalindrome(1, true);
    verifyPalindrome(11, true);
    verifyPalindrome(10, false);
    verifyPalindrome(100, false);
    verifyPalindrome(101, true);
    verifyPalindrome(1001, true);
    verifyPalindrome(1021, false);
    verifyPalindrome(12321, true);
    verifyPalindrome(12331, false);
    verifyPalindrome(123321, true);
    verifyPalindrome(123421, false);
    verifyPalindrome(12344321, true);
    verifyPalindrome(12343321, false);
    verifyPalindrome(1222, false);
    verifyPalindrome(111111, true);
  }

  private static void verifyPalindrome(int number, boolean expected) {
    final boolean actual = isPalindrome(number);
    System.out.println("Is " + number + " a palindrome? " + actual + "  " + (actual == expected ? "OK" : "**ERROR**"));
  }

  private static void doProblem() {
    List<Integer> sortedPals = palindromes(MIN_NUM, MAX_NUM);
    System.out.println("Largest pal: " + sortedPals.get(sortedPals.size() - 1));
  }

  private static List<Integer> palindromes(int min, int max) {
    final List<Integer> list = new ArrayList<>();
    for (int i = max; i >= min; i--) {
      for (int j = max; j >= i; j--) {
        if (isPalindrome(i*j)) {
          list.add(i*j);
        }
      }
    }
    Collections.sort(list);
    return list;
  }

  private static boolean isPalindrome(int num) {
    final int N_DIGITS = 10;
    final int[] digits = new int[N_DIGITS];  // 32-bit integers can hold up to single billions, i.e. 10 digits

    int highestDigit = 0; // index of the highest non-zero digit
    // start from the right-most digit
    for (int i = 0; i < N_DIGITS; i++) {
      highestDigit = i;
      digits[i] = num % 10;
      num /= 10;

      if (num == 0) { // no more non-zero digits
        break;
      }
    }

    // compare digits for symmetry
    final int n = (highestDigit + 1); // 0-index to 1-index
    for (int i = 0; i < n/2; i++) {
      if (digits[i] != digits[n-i-1]) {
        return false;
      }
    }
    return true;
  }
}


