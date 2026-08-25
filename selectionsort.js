let array= [1, 2, 43, 32, 100, 12];
let n = array.length;

for (let i = 0; i < n - 1; i++) {
  let min = i;

  for (let j = i + 1; j < n; j++) {
    if (array[j] < array[min]) {
      min = j;
    }
  }

  let temp = array[i];
  array[i] = array[min];
  array[min] = temp;
}

console.log(array);
