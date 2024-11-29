<?php
function calculate_pi($iterations)
{
  $pi = 0;
  for ($i = 0; $i < $iterations; $i++) {
    $term = pow(-1, $i) / (2 * $i + 1);
    $pi += $term;
  }
  return 4 * $pi;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (isset($_POST['iterations']) && is_numeric($_POST['iterations'])) {
    $iterations = intval($_POST['iterations']);
    if ($iterations > 0) {
      $pi_value = calculate_pi($iterations);
      echo "<h1>Approximation of π</h1>";
      echo "<p>Number of iterations: $iterations</p>";
      echo "<p>Approximated value of π: $pi_value</p>";
      echo '<a href="index.html">Back to Calculator</a>';
    } else {
      echo "<p>Please enter a positive integer greater than 0.</p>";
      echo '<a href="index.html">Back to Calculator</a>';
    }
  } else {
    echo "<p>Invalid input. Please enter a positive integer.</p>";
    echo '<a href="index.html">Back to Calculator</a>';
  }
}
