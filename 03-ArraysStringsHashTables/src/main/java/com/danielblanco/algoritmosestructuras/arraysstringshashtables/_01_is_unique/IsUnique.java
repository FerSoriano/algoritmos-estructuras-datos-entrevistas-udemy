package com.danielblanco.algoritmosestructuras.arraysstringshashtables._01_is_unique;

import java.util.HashSet;
import java.util.Set;

/*
 * Dado un método que recibe una String, comprobar si todos los caracteres son únicos o no.
 *
 * isUnique("abcde") => true;
 * isUnique("abcded") => false;
 */
public class IsUnique {

  private static final int NUMBER_OF_CHAR = 128; // ASCII

  public boolean isUnique(String s) {
    if (s.length() > NUMBER_OF_CHAR)
      return false;

    Set<Character> chars = new HashSet<>();
    for (Character c : s.toCharArray()) {
      if (chars.contains(c))
        return false;
      chars.add(c);
    }

    return true;
  }
}
