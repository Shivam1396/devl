let a = [1, 2, 43, 32, 100, 12];
let n = a.length;

for (let i = 0; i < n - 1; i++) {
  let min = i;

  for (let j = i + 1; j < n; j++) {
    if (a[j] < a[min]) {
      min = j;
    }
  }

  let temp = a[i];
  a[i] = a[min];
  a[min] = temp;
}

console.log(a);